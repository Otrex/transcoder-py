#!/usr/bin

import subprocess
import requests
import os

space = "https://dumo-cloud-lms.fra1.digitaloceanspaces.com"
downloadPath = 'downloadedVideos'
transcodedPath = 'transcodedVideos'
_dirname = os.path.dirname(__file__)

def shell(*args):
  run = subprocess.run(list(args), stdout=subprocess.PIPE, check=True)
  if run.stderr != None: print(run.stderr)
  print('--------------------------Task Complete-------------------------------')

def download (url):
  shell('wget', '-P', downloadPath, f"{space}/{url}")
  print('--------------------------Download Complete---------------------------')

videos = [
  "lecture-contents/5afb9f59-103f-4bbb-8b99-7d6aae1d04ae",
  "lecture-contents/8153ee11-865e-4d37-b2ac-fc3b4ad9987f",
  "lecture-contents/25c47f70-f7e5-42e2-94fa-1de95d9bdda0",
  "lecture-contents/d5153505-57bd-49b4-b49b-a5c4ad716acc",
  "lecture-contents/5aef4f73-c79c-4f57-8abd-84cf553cb28b",
  "lecture-contents/42e2bc74-2bd0-4f35-9132-ea29a5cfab44",
  "lecture-contents/f170ee15-ec3e-4894-9407-9af6cf892fba"
]

for url in videos:
  try:
    download(url)
  except:
    path = os.path.join(_dirname, downloadPath, url.split('/')[-1])
    if os.path.exists(path):
      os.remove(path)

shell("bash", 'trancoderv2.sh', downloadPath , transcodedPath )