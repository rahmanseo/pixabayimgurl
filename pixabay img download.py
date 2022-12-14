from requests import get
from pprint import pprint
api_key = "32063034-fc889e3c9cc03533a70dad8f1"
quary = "yellow+flowers"
api_url = f"https://pixabay.com/api/?key={api_key}&q={quary}"
res = get(api_url)
api_data = res.json().get("hits")
for data in api_data:
    img_url = data.get ('webformatURL')
    file = open("img.txt","a+")
    file.writelines(img_url+'\n')
    file.close()