from ocr import image_to_string

_ = image_to_string(open("captcha2.jpg", "rb"))
print(_)