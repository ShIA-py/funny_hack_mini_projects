# client
import socket
import pyautogui
import io
import time

def connect_to_server():
    while True:
        try:
            client = socket.socket()
            client.connect(('192.168.0.100', 12345))
            print("Успешно подключились к серверу!")
            return client
        except Exception as e:
            print(f"Не удалось подключиться: {e}. Повторная попытка через 3 секунды...")
            time.sleep(3)

print("Ожидаем подключение к серверу...")
client = connect_to_server()
print("Начали трансляцию...")

try:
    while True:
        try:
            screenshot = pyautogui.screenshot()
            img_bytes = io.BytesIO()
            screenshot.save(img_bytes, format='PNG')
            img_data = img_bytes.getvalue()

            # Отправляем размер и данные
            client.send(len(img_data).to_bytes(4, 'big'))
            client.send(img_data)

            time.sleep(0.05)

        except (ConnectionError, BrokenPipeError):
            print("Соединение разорвано. Переподключаемся...")
            client.close()
            client = connect_to_server()

except KeyboardInterrupt:
    print("Остановка...")
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    client.close()