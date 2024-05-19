import requests
import schedule
import time
import openai
import logging
from datetime import datetime

# Configuración de las APIs
FACEBOOK_ACCESS_TOKEN = 'YOUR_FACEBOOK_ACCESS_TOKEN'
PAGE_ID = 'YOUR_PAGE_ID'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
PAGE_NAME = 'YOUR_PAGE_NAME'  # Nombre de la fanpage

# Configuración de OpenAI
openai.api_key = OPENAI_API_KEY

# Configuración del registro (log)
logging.basicConfig(filename='publicaciones.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generar_post():
    prompt = "Escribe una publicación sobre XXXX."
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        post_text = response.choices[0].text.strip()
        return post_text
    except Exception as e:
        logging.error(f"Error generando el post: {e}")
        return None

def publicar_post():
    post_text = generar_post()
    if not post_text:
        return
    
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    params = {
        'message': post_text,
        'access_token': FACEBOOK_ACCESS_TOKEN
    }
    
    try:
        response = requests.post(url, params=params)
        if response.status_code == 200:
            logging.info(f"Publicado en {PAGE_NAME}: {post_text}")
        else:
            logging.error(f"Error al publicar en {PAGE_NAME}: {response.text}")
    except Exception as e:
        logging.error(f"Error al hacer la solicitud de publicación: {e}")

# Programar publicaciones 3 veces al día
schedule.every().day.at("09:00").do(publicar_post)
schedule.every().day.at("13:00").do(publicar_post)
schedule.every().day.at("17:00").do(publicar_post)

while True:
    schedule.run_pending()
    time.sleep(1)
