import math

procents = int(input())
money = int(input())

assert 1 <= procents <= 99
assert 10 ** 5 <= money <= 10 ** 9

print(math.ceil(money*(procents/100)))
