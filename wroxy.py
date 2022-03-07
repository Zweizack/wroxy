#!/usr/bin/env python3
# -*- coding: utf-8 -*-

title = """ __       __                                     
|  \\  _  |  \\                                    
| ▓▓ / \\ | ▓▓ ______   ______  __    __ __    __ 
| ▓▓/  ▓\\| ▓▓/      \\ /      \\|  \\  /  \\  \\  |  \\
| ▓▓  ▓▓▓\\ ▓▓  ▓▓▓▓▓▓\\  ▓▓▓▓▓▓\\\\▓▓\\/  ▓▓ ▓▓  | ▓▓
| ▓▓ ▓▓\\▓▓\\▓▓ ▓▓   \\▓▓ ▓▓  | ▓▓ >▓▓  ▓▓| ▓▓  | ▓▓
| ▓▓▓▓  \\▓▓▓▓ ▓▓     | ▓▓__/ ▓▓/  ▓▓▓▓\\| ▓▓__/ ▓▓
| ▓▓▓    \\▓▓▓ ▓▓      \\▓▓    ▓▓  ▓▓ \\▓▓\\\\▓▓    ▓▓
 \\▓▓      \\▓▓\\▓▓       \\▓▓▓▓▓▓ \\▓▓   \\▓▓_\\▓▓▓▓▓▓▓
                                       |  \\__| ▓▓
                                        \\▓▓    ▓▓
                                         \\▓▓▓▓▓▓ 
"""

import os, platform, json, requests
from socket import timeout

bold = "\033[1m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[97m"

try:
  if (platform.system() == 'Windows'):
    os.system('cls')
  else:
    os.system('clear')

  print(bold+green+title)
  print(cyan+'-' * 0x33)

  array = []
  with open('list.txt') as f:
    for line in f:
      array.append(line)
    for i in array:
      try:
        proxies = {
          'http': 'http://'+i.strip(),
        }

        req = requests.Session()
        res = req.post('http://ip-api.com/json?fields=status,countryCode,query', proxies=proxies, timeout=1.5).json()
        res = json.loads(json.dumps(res))
        if (res['status'] == 'success'):
          saved = open('proxy.txt', 'a')
          saved.write(f'{i.strip()}\n')
          saved.close()
          print(f"{cyan}PROXY {green}ACTIVE {white}[{magenta}{res['countryCode']}{white}] {yellow}{res['query']}")
      except (ValueError, requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        continue

except KeyboardInterrupt:
  exit(red+"\n[!] STOP")
