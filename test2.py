import json
import requests
from selenium import webdriver

with open('./output/', 'w') as outfile:
    json.dump('json', outfile)