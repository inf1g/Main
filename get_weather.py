import requests


def get_weather(location):
    url = 'https://wttr.in'
    payload = "TMqn&lang=ru"
    response = requests.get(f"{url}/{location}", params=payload)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    locations = ["london", "svo", "Череповец"]
    for loc in locations:
        print(get_weather(loc))
