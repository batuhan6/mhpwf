from Pathlib import Path
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
    
