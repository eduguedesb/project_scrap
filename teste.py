from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def extrair_urls(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')  # Para executar o navegador em modo headless (sem janelas visíveis)
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    except TimeoutException as errt:
        print("Timeout de Solicitação:", errt)
        return []

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = soup.find_all('a')
    
    urls = [link.get('href') for link in links if link.get('href')]
    
    driver.quit()
    
    return urls

# Solicitar a URL ao usuário
url_alvo = "https://www.webglobal.com.br/carreiras"

# Chamar a função para extrair as URLs
urls_capturadas = extrair_urls(url_alvo)

# Salvar a lista de URLs em um arquivo de texto
with open('urls.txt', 'w') as file:
    for url in urls_capturadas:
        file.write(url + '\n')

print("Lista de URLs capturadas salva em 'urls.txt'.")