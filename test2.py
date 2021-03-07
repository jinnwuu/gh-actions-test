import json
import requests
from selenium import webdriver

with open('./output/test.json', 'w') as outfile:
    json.dump('json', outfile)