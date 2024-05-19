# Auto Facebook Poster

Este script está diseñado para publicar automáticamente en una página de Facebook tres veces al día sobre cualquier tema que desees. Utiliza la API de OpenAI para generar contenido único en cada publicación según el prompt proporcionado.

## Características

- Publica automáticamente en una página de Facebook tres veces al día (09:00, 13:00 y 17:00).
- Genera contenido único para cada publicación utilizando la API de OpenAI.
- Registra todas las publicaciones y errores en un archivo de log.

## Requisitos

- Python 3.x
- Bibliotecas: `requests`, `schedule`, `openai`, `logging`
- Acceso a la API de Facebook y OpenAI

## Configuración

1. **Clonar el repositorio:**

   ```sh
   git clone https://github.com/byvelvet/Automated-Fb-Post-with-OpenAI.git
   cd tu_repositorio

   Instalar las dependencias:

sh
Copiar código
pip install requests schedule openai
Configurar las credenciales:

Edita el archivo post_facebook.py y reemplaza las siguientes variables con tus credenciales:

python
Copiar código
FACEBOOK_ACCESS_TOKEN = 'YOUR_FACEBOOK_ACCESS_TOKEN'
PAGE_ID = 'YOUR_PAGE_ID'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
PAGE_NAME = 'YOUR_PAGE_NAME'
Configurar el prompt:

Edita el archivo post_facebook.py y reemplaza el contenido del prompt en la función generar_post para el tema deseado:

python
Copiar código
def generar_post():
    prompt = "Crea un post sobre el tema que desees aquí."
    
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
