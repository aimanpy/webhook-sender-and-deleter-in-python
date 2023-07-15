import requests
import json

def enviar_mensaje(webhook_url, contenido):
    payload = {
        "content": contenido
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    if response.status_code == 204:
        print("Mensaje enviado con éxito.")
    else:
        print(f"Error al enviar el mensaje. Código de estado: {response.status_code}")

def eliminar_webhook(webhook_url):
    response = requests.delete(webhook_url)

    if response.status_code == 204:
        print("Webhook eliminado con éxito.")
    else:
        print(f"Error al eliminar el webhook. Código de estado: {response.status_code}")

# Ejemplo de uso
webhook_url = input("Ingresa la URL del webhook: ")
contenido_mensaje = input("Ingresa el contenido del mensaje: ")

enviar_mensaje(webhook_url, contenido_mensaje)

opciones_validas = ['Y', 'N']
opcion_eliminar = input("¿Deseas eliminar este webhook? (Y/N): ")

while opcion_eliminar not in opciones_validas:
    print("Opción inválida. Intenta nuevamente.")
    opcion_eliminar = input("¿Deseas eliminar este webhook? (Y/N): ")

if opcion_eliminar == 'Y':
    eliminar_webhook(webhook_url)
else:
    print("El webhook no será eliminado.")
