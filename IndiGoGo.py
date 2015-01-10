#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib import urlopen

URL = 'https://www.indiegogo.com/project/builder-an-ide-of-our-gnome/embedded/8947753'

f = urlopen(URL)
data = f.read()
soup = BeautifulSoup(data, 'html.parser')
amount = soup.find(**{'class': 'currency currency-medium'}).span.text
fraction = int(''.join([c for c in amount if c in '0123456789'])) / 30000.

print ('''{"raised": "%s", "fraction": %f}''' % (amount, fraction))
