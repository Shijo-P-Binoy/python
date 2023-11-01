import qrcode

user_in=input("Enter a link for the QRcode generator :")
file_out=input("Enter the filename (Eg: qrcode.png) :")

features = qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data(user_in)
features.make(fit=True)

generate_image = features.make_image()
generate_image.save(file_out)
print(f"QR code is saved as {file_out}")