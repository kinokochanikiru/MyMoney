import requests
import json

def test():
    url = "http://127.0.0.1:8000"
    data = {
        "x": 1,
        "y": 3,
    }
    response = requests.post(url, json=data)
    print(response.json())

if __name__ == "__main__":
    test()
