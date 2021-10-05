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
  "lecture-contents/5aef4f73-c79c-4f57-8abd-84cf553cb28b",
  "lecture-contents/42e2bc74-2bd0-4f35-9132-ea29a5cfab44",
  "lecture-contents/bef1a49d-5025-4d0b-9137-b910f95768f9",
  "lecture-contents/9f05a0c3-55a8-4795-960b-0d75a753e743",
  "lecture-contents/866bbc92-8129-49d2-86ec-73180ebfa6dc",
  "lecture-contents/cb8e58d7-dbe7-44b1-a59e-218adb9512fe",
  "lecture-contents/e4e3ec62-ab03-46bb-b45a-61c2a29fcb4d",
  "lecture-contents/34b94cd6-503e-417d-8f0c-3d1e32379d63"
]

for url in videos:
  try:
    download(url)
  except:
    path = os.path.join(_dirname, downloadPath, url.split('/')[-1])
    if os.path.exists(path):
      os.remove(path)

shell("bash", 'trancoderv2.sh', downloadPath , transcodedPath )