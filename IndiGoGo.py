#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib import urlopen

URL = 'https://www.indiegogo.com/project/builder-an-ide-of-our-gnome/embedded/8947753'

# Define variables
f = urlopen(URL)
data = f.read()
soup = BeautifulSoup(data, 'html.parser')
amount = soup.find(**{'class': 'currency currency-medium'}).span.text

body_open_tag = '''<!DOCTYPE html">
<html>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
<head>
  <title>Builder Fundraiser</title>
</head>
<body align=center>'''

heading='''
<img src="https://wiki.gnome.org/Apps/Builder?action=AttachFile&do=get&target=splash.png"><img></br>
<button style="font-family:Charcoal, sans-serif; padding: 20px 100px;background: #f9f9f9; color: #000; font-size:16px; border-radius:6px;"><a href="https://www.indiegogo.com/projects/builder-an-ide-of-our-gnome">Donate</a></button>
'''

raised_open_tag ='''<div class="progress" style="width:600px; text-align:center;">
  <div class="progress-bar progress-bar-success" role="progressbar" style="width:40%">
  </div>
  <div class="progress-bar progress-bar-warning" role="progressbar" style="width:20%">
    Nearly There!
  </div>
  <div class="progress-bar progress-bar-danger" role="progressbar" style="width:2%; color:#000;">'''
raised_close_tag =''' Raised so far!
  </div>
</div><p style="font-family:Impact, Charcoal, sans-serif">'''

body_close_tag='''
</body>
</html>
'''

contents = body_open_tag + heading + raised_open_tag + amount + raised_close_tag + body_close_tag

def main():
  local_browser(contents)

def string_to_file(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def local_browser(webpageText, filename='temp.html'):
    '''File at '''
    import webbrowser, os.path
    string_to_file(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))

main()
