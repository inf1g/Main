import requests


def weather(location):
    url = 'https://wttr.in'
    payload = "?TMqn&lang=ru"
    response = requests.get(url)
    response.raise_for_status()
    if response.ok:
        response = requests.get(f"{url}{location}", params=payload)
        return response.text
    else:
        return response.status_code


if __name__ == '__main__':
    print(weather("/london"))
    print(weather("/svo"))
    print(weather("/Череповец"))
