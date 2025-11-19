
import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
   
    hrefs = []
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            html_content = response.text
            hrefs = re.findall(r'<a\s+(?:[^>]*?\s+)?href="([^"]+)"', html_content)
        else:
            print(f"Chyba: stránka vrátila status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Chyba při stahování stránky: {e}")
    return hrefs

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        links = download_url_and_get_all_hrefs(url)
        print("Nalezené odkazy:")
        for link in links:
            print(link)
    except Exception as e:
        print(f"Program skončil chybou: {e}")
