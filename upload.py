import requests
import urllib.parse
import os


def upload():
    file_path = 'output/'+os.listdir('output')[0]
    if file_path:
        file_name = os.path.basename(file_path)
        encoded_name = urllib.parse.quote(file_name)
        url = f"https://filebin.net/{os.urandom(5).hex()}/{encoded_name}"
        with open(file_path, 'rb') as f:
            response = requests.post(url, data=f)
        print("\nStatus Code:", response.status_code)
        print("Response Text:", response.text)
        print(url)
    else:
        print("No file selected.")

upload()
