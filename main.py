import requests
import http.client

def get_info(ip):
    try:
        responce = requests.get(url = f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': responce.get('query'),
            '[Country]': responce.get('country'),
            '[City]': responce.get('city'),
            '[Prov]': responce.get('isp'),
        }

        for k, v in data.items():
            print(f'{k}: {v}')

    except requests.exceptions.ConnectionError:
        print('Error')

def main():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    ip = conn.getresponse().read()
    ip = str(ip)[2:-1]

    get_info(ip)

if __name__ == '__main__':
    main()
