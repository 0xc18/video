import requests
import urllib.parse
import os

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def upload():
    file_path = 'output/'+os.listdir('output')[0]
    if file_path:
        file_name = os.path.basename(file_path)
        encoded_name = urllib.parse.quote(file_name)
        url = f"https://filebin.net/{os.urandom(5).hex()}/{encoded_name}"
        with open(file_path, 'rb') as f:
            response = requests.post(url, data=f,proxies=proxies)
        print("\nStatus Code:", response.status_code)
        print("Response Text:", response.text)
        print(url)
    else:
        print("No file selected.")

upload()
