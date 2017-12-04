import math

coords = input().split(" ")
coords = [int(i) for i in coords]

assert len(coords) == 4
for i in coords:
    assert i <= 1000

print(round(math.sqrt((coords[2]-coords[0])**2+(coords[3]-coords[1])**2)))
