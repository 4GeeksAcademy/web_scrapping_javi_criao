import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

url = "https://www.compraonline.alcampo.es/categories/bebidas/cervezas/cerveza-lata-est%C3%A1ndar/OC110701"
response = requests.get(url)
html_content = response.text
print(f"HTML descargado. Estado: {response.status_code}")

