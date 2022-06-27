from re import search
from ast import literal_eval
from bs4 import BeautifulSoup as Bs


def allhen_parse(response_text: str):
    soup = Bs(response_text, "lxml")
    comix_name = soup.find("a", class_='manga-link').text
    re_expr = r'initReader\(.*(\[\[.+\]\]).*\)'
    match = search(re_expr, response_text)
    json_text = match.group(1)
    json_data = literal_eval(json_text)
    pics_list = [('https://' + (data_url[1] + (data_url[0] + data_url[2])).lstrip('//')) for data_url in json_data]
    res = {"name": comix_name, "pics_list": pics_list}
    return res
