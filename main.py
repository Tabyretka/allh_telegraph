import parser
import requests
from telegraph import Telegraph

telegraph = Telegraph()


def main(url: str) -> str:
    try:
        headers = {
            "user-agent": "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0"
        }
        session = requests.Session()
        rs = session.get(url=url, headers=headers)

        if rs.ok:
            telegraph.create_account(short_name='Noa19')
            n = parser.allhen_parse(rs.text)

            html = f'<a href="{url}">ALLHEN</a><br>'
            for photo in n["pics_list"]:
                html += f"<img src='{photo}'/><br>"

            response = telegraph.create_page(
                f'{n["name"] + url.split("/")[-1]}',
                html_content=html)
            return 'http://telegra.ph/{}'.format(response['path'])

        else:
            return str(rs.status_code)
    except Exception as ex:
        return f"{ex}"


if __name__ == "__main__":
    url = input("Enter a url:\n")
    print(main(url=url))
