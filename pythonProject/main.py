import qrcode

# duhankosali
code = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=100, # boyut
    border=4 # kenar kalınlığı
)

url= input("URL Giriniz: ")

code.add_data(url)
code.make(fit=True)

image = code.make_image(fill_color = "black",back_color="white")
image.save("qrcode.png")

