from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests, os, time

url = "https://www.constituteproject.org/constitutions?lang=en&status=in_force&status=is_draft"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(5)  

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

os.makedirs("constitutions_pdfs", exist_ok=True)
base = "https://www.constituteproject.org"

pdf_links = []
for a in soup.find_all("a", href=True):
    href = a["href"]
    if href.endswith(".pdf"):
        pdf_links.append(base + href if href.startswith("/") else href)

print(f"Found {len(pdf_links)} constitutions.")

for link in pdf_links:
    filename = link.split("/")[-1]
    path = os.path.join("constitutions_pdfs", filename)
    if os.path.exists(path):
        continue
    print(f"Downloading {filename}...")
    r = requests.get(link, stream=True)
    with open(path, "wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    time.sleep(1)
