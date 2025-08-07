import requests
import time

# Remplace cette URL par celle de ton site
URL = "https://novaai-9urt.onrender.com/"

def keep_awake():
    try:
        response = requests.get(URL)
        print(f"{time.ctime()} - Visite envoyée - Status: {response.status_code}")
    except Exception as e:
        print(f"{time.ctime()} - Erreur lors de la requête: {e}")

if __name__ == "__main__":
    keep_awake()
