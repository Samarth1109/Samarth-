import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)
qr.add_data("https://www.instagram.com/thee.samarthh/profilecard/?igsh=MTl2YXdqMGQ5ejdheA==")
qr.make(fit=True)
img=qr.make_image(fill_color="black",bg_color="white")
img.save("instagram.png")

