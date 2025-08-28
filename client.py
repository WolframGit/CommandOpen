import socket
import platform
import os
from time import sleep as s

SYSTEM = platform.system()
RECV = 1024

def terminal_cleaner():
    if SYSTEM == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def ip_validate(ip):
    try:
        if socket.inet_aton(ip):
            return True
    except socket.error:
        return False

def client_starter(host, port: int = 8000):
    try:
        if not ip_validate(host):
            client_starter(str(input('Введите локальный IP для подключения: ')))
        
        terminal_cleaner()
        print(f'Вы успешно подключились к {host}:{port}.')

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        print('\nДля получения команд - /help.\n')

        while True:
            command = input('-> ')
            client.send(command.encode('utf-8'))

            response = client.recv(1024).decode('utf-8')
            print(f'\n{response}\n')

    except KeyboardInterrupt:
        print('\nПроизошла ошибка...\nПерезапуск через 2 секунды.')
        s(2)
        terminal_cleaner()
        client_starter(str(input('Введите локальный IP для поключения: ')))

if __name__=='__main__':
    terminal_cleaner()
    client_starter(str(input('Введите локальный IP для поключения: ')))