import random
import json

f = open('json.json', 'a')


def generate(x, y):
    str = input("Enter a text (or number): ")
    length = len(str)
    h = x + y + length
    h = h * x
    h = h + y
    s = random.randint(1,100)
    h = h + s
    return h
for i in range(0,10):
     a = generate(random.randint(1,100),random.randint(1,100))
     f.write(str(a))

f.close()

