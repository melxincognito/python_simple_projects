import pyqrcode

from pyqrcode import QRCode

s = 'www.melxincognito.com'
url = pyqrcode.create(s)

url.svg("myqr.svg", scale = 8)
url.png("myqr.png", scale = 6)

# pip install pyqrcode