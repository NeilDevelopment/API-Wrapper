import requests

class Status:
    def stellular():
        resp = requests.get("https://api.neildevelopment.xyz/status/stellular")
        json = resp.json()
        return json

    def docs():
        resp = requests.get("https://api.neildevelopment.xyz/status/docs")
        json = resp.json()
        return json

    def cdn():
        resp = requests.get("https://api.neildevelopment.xyz/status/cdn")
        json = resp.json()
        return json
