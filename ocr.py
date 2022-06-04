from requests import post
from base64 import b64encode

API_KEY = ""

def image_to_string(img):
    img = b64encode(img.read()).decode("ascii")
    data = {
        "apikey": API_KEY,
        "base64image": "data:image/png;base64," + img
    }
    with post("https://api.ocr.space/parse/image", data=data) as response:
        return response.json()["ParsedResults"][0]["ParsedText"]