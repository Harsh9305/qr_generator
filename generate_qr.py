import qrcode
import sys

def generate_qr(data: str, output_file: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(output_file)
    print(f"QR Code generated and saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_qr.py <data_to_encode> <output_file>")
    else:
        data = sys.argv[1]
        output_file = sys.argv[2]
        generate_qr(data, output_file)
