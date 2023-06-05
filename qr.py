import os
import qrcode

counter = 1

def generate_qr_code(text):
    global counter
    qr = qrcode.QRCode(
        version=40,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    while True:
        filename = f"qrcode-{counter}.png"
        if not os.path.exists(filename):  # Check if the file already exists
            qr_img.save(filename)
            break
        counter += 1
    
    counter += 1
    return qr_img

text = input("Enter the text to convert to QR code: ")

qr_code = generate_qr_code(text)