import requests


def weather(location):
    url = 'https://wttr.in'
    payload = "?TMqn&lang=ru"
    response = requests.get(f"{url}{location}", params=payload)
    response.raise_for_status()
    return response.text



if __name__ == '__main__':
    print(weather("/london"))
    print(weather("/svo"))
    print(weather("/Череповец"))
