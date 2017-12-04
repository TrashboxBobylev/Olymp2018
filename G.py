length = int(input())
numbers = input().split(" ")

numbers = [int(i) for i in numbers]

assert 1 <= length <= 5000
assert len(numbers) == length

for i in numbers:
    assert i <= 2**31 - 1

numbers.sort()

if length % 2:
    print('{:.1f}'.format(numbers[int((length/2))]))
else:
    print('{:.1f}'.format((numbers[int(length/2)]+numbers[int(length/2-1)])/2))
