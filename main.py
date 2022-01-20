from pathlib import Path
import requests
import json
import os

try:
    base_dir = Path(__file__).resolve().parent
    jsons_dir = Path.joinpath(base_dir, 'JsonFiles')
    os.mkdir('JsonFiles')
except FileExistsError:
    pass

while True:
    endpoint = input("Lutfen api endpointini giriniz! Ya da cikmak icin exit yaziniz: ")
    connect_api = requests.get(f"https://jsonplaceholder.typicode.com/{endpoint}")

    if connect_api.status_code == 200:
        data = connect_api.json()
        try:
            with open(f"{jsons_dir}/{endpoint}.json","r") as f:
                answer = input("Bu dosya zaten mevcut. Uzerine mi yazilsin mevcut dosyaya ekleme mi yapilsin?     uzerine/ekleme: ")
                if answer == 'uzerine':
                    with open(f"{jsons_dir}/{endpoint}.json",'w') as f:
                        json.dump(data, f, sort_keys=True, indent=4)
                else:
                    with open(f"{jsons_dir}/{endpoint}.json", 'a') as f:
                        json.dump(data, f, sort_keys=True, indent=4)
        except FileNotFoundError:
            with open(f"{jsons_dir}/{endpoint}.json",'w') as f:
                json.dump(data, f, sort_keys=True, indent=4)

    elif endpoint == 'exit':
        break

    else:
        print("Hatali endpoint girdin.")
        print("y")
