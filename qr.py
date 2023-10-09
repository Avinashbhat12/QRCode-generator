import qrcode
generate =qrcode.make("Avinash bhat")
feature=qrcode.QRCode(box_size=40,border=2)
feature.add_data('https://www.linkedin.com/in/avinash-bhat-b86558255/')
feature.make(fit=True)
generate=feature.make_image(fill_color="black",back_color="white")
generate.save('image3.png')