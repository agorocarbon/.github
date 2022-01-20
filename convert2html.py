from json2html import *
import sys

file = open(sys.argv[1], "r")
results = file.read()

print(json2html.convert(json=results))
