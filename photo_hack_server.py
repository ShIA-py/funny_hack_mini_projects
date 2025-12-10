# server (('192.168.0.102', 12345))
import socket
import pygame
import io
from PIL import Image

pygame.init()
screen = pygame.display.set_mode((800, 600))

server = socket.socket()
server.bind(('192.168.0.100', 12345))
server.listen(1)
client, addr = server.accept()
print(f"Подключен: {addr}")

running = True
while running:
    # Обрабатываем ВСЕ события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    try:
        # Просто пытаемся получить данные
        size_data = client.recv(4)
        if size_data:
            size = int.from_bytes(size_data, 'big')
            image_data = client.recv(size)

            img = Image.open(io.BytesIO(image_data))
            img = img.resize((800, 600))
            py_image = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
            screen.blit(py_image, (0, 0))
            pygame.display.flip()

    except:
        pass

pygame.quit()