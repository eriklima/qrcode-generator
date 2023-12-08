import os
import qrcode
import csv
import shutil

PASTA_QRCODES = r"../qrcodes_gerados"
ARQUIVO_CONTATOS = r"../contatos.csv"


def main():
    limpar_pasta_qrcodes()

    colaboradores = obter_lista_colaboradores()

    criar_qrcodes(colaboradores)


def limpar_pasta_qrcodes():
    nome_pasta = os.path.join(os.path.dirname(__file__), PASTA_QRCODES)
    shutil.rmtree(nome_pasta)
    os.makedirs(nome_pasta)


def obter_lista_colaboradores():
    caminho_csv_projetos = os.path.join(os.path.dirname(__file__), ARQUIVO_CONTATOS)
    colaboradores = ler_csv_colaboradores(caminho_csv_projetos)
    
    del colaboradores[0] # Deleta a primeira linha do CSV (nomes das colunas)

    return colaboradores


def ler_csv_colaboradores(caminho_arquivo_csv):   
    with open(caminho_arquivo_csv, newline='') as arquivo_csv:
        linhas = csv.reader(arquivo_csv, delimiter=';') 
        linhas = list(linhas) # Coloca as linhas numa lista
        
        colaboradores = []
        
        for linha in linhas:
            colaboradores.append(linha)
        
    return colaboradores


def criar_qrcodes(colaboradores):
    for colaborador in colaboradores:
        empresa = colaborador[0]
        nome_completo = colaborador[1]
        email = colaborador[2]
        cargo = colaborador[3]
        telefone = colaborador[4]
        site = colaborador[5]

        print("Gerando QrCode para: " + nome_completo)
    
        qrcode_data = create_vcard_data(empresa, nome_completo, cargo, email, telefone, site)
        qrcode_image_path = os.path.join(os.path.dirname(__file__), PASTA_QRCODES, f"{nome_completo}.png")

        create_qrcode_to_image(qrcode_data, qrcode_image_path)


def create_vcard_data(empresa, nome_completo, cargo, email, telefone, site):
    data = f'''BEGIN:VCARD\nVERSION:3.0\nORG:{empresa}\nFN:{nome_completo}\nTITLE:{cargo}\nEMAIL:{email}\nTEL;WORK;VOICE:{telefone}\nURL:{site}\nEND:VCARD'''
    return data


def create_qrcode_to_image(data, image_path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(image_path)


if __name__ == '__main__':
    main()
