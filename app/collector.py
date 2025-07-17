import requests
import json
import time
from datetime import datetime

def get_crypto_data():
    """
    Obtém dados de criptomoedas da API da Coinbase.
    """
    url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para códigos de status HTTP ruins (4xx ou 5xx)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados da API: {e}")
        return None

def save_data_to_landing(data):
    """
    Salva os dados na camada de landing.
    """
    if data:
        # Adiciona o timestamp ao dicionário de dados
        data['timestamp'] = datetime.now().isoformat()

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"data/landing/crypto_data_{timestamp}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Dados salvos em {filename}")

if __name__ == "__main__":
    while True:
        crypto_data = get_crypto_data()
        save_data_to_landing(crypto_data)
        time.sleep(60)  # Espera 60 segundos antes da próxima coleta
