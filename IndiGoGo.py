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
<head>
  <title>Builder Fundraiser</title>
</head>
<body align=center>'''

heading='''<h1>GNOME Builder Fundraiser.</h1>
           <h2><a href="https://www.indiegogo.com/projects/builder-an-ide-of-our-gnome">Please Donate!</a></h2>'''

raised_open_tag ='''<h3>'''
raised_close_tag =''' Raised So Far!</h3>'''

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
