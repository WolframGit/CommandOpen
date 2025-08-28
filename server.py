import socket
import platform
import os
import webbrowser
from time import sleep as s

SYSTEM = platform.system()
RECV = 1024
COMMAND = ()
HELP_TEXT = '''Сайты:
    Открыть YouTube - /YouTube
    Открыть Deepseek - /Deepseek
    soon...'''

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

def server_starter(port: int = 8000):
    try:
        ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip.connect(('8.8.8.8', 8000))
        host = ip.getsockname()[0]
        ip.close()

        print(f'Твой локальный айпи -> {host}')
        if not ip_validate(host):
            return False
        pass
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        print(f'Ожидаем запрос на {host}:{port}...')
        server.listen()

        while True:
            user, addr = server.accept()
            print(f'\nYou are connected! Your port a connection -> {addr[1]}')

            while True:
                data = user.recv(RECV).decode('utf-8').strip()

                if data == '/help':
                    help_text = '''Сайт:
    Чтобы открыть сайт, напишите /open [название сайта].'''
                    user.sendall(help_text.encode('utf-8'))
                    continue

                if not data:
                    break
                
                elif data.startswith('/open'):
                    reopen = data.split()

                    if len(reopen) < 2:
                        user.sendall(f'Команда "{data}" является недействительной...'.encode('utf-8'))
                        continue
                    
                    site_name = reopen[1]
                    open_website = webbrowser.open(f'https://{site_name}.com')
                    if open_website:
                        user.sendall(f'Сайт: "{site_name}" был успешно открыт!'.encode('utf-8'))
                        continue
                
                #Старт будет добавлен в следующем обновлении (принадлежит открытию всяких програм!)
                elif data.startswith('/open') != True or data.startswith('/start') != True:
                        user.sendall(f'Команды {data} не существует!\nПовторите попытку...'.encode('utf-8'))
                        continue

    except KeyboardInterrupt:
        print('Произошла ошибка...\nВыходим через 2 секунды...')
        s(2)
        terminal_cleaner()

if __name__=='__main__':
    terminal_cleaner()
    server_starter()

