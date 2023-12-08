import os
import qrcode

empresa = "Near Location"
nome_completo = "Erik Lima"
cargo = "Tech Lead"
email = "erik.lima@nearlocation.com.br"
telefone = "48 3233-1031"
site = "www.nearlocation.com.br"


def main():
    qrcode_data = create_vcard_data(empresa, nome_completo, cargo, email, telefone, site)
    qrcode_image_path = os.path.join(os.path.dirname(__file__), "../qrcodes_gerados/qrcode.png")

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
