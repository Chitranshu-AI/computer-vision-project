from barcode import EAN13
from barcode.writer import ImageWriter

number = '59083298'
my_code = EAN13(number, writer=ImageWriter())

my_code.save("barcode")