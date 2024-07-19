import requests
from bs4 import BeautifulSoup

def extrair_urls(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.5'
    }
    
    # Adiciona o prefixo "http://" se não estiver presente na URL
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    
    try:
        resposta = requests.get(url, headers=headers, timeout=5)
        resposta.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Erro de Conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout de Solicitação:", errt)
    except requests.exceptions.RequestException as err:
        print("Erro na Solicitação:", err)
        return []

    urls = []

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href:
                urls.append(href)
    else:
        print(f"Erro ao acessar a página. Código de status: {resposta.status_code}")

    return urls

# Solicitar a URL ao usuário
url_alvo = input("Digite a URL que deseja fazer scraping (apenas a partir do 'www.'): ")

# Chamar a função para extrair as URLs
urls_capturadas = extrair_urls(url_alvo)

# Salvar a lista de URLs em um arquivo de texto
with open('urls.txt', 'w') as file:
    for url in urls_capturadas:
        file.write(url + '\n')

print("Lista de URLs capturadas salva em 'urls.txt'.")
