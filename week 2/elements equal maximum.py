x = int(input())
max = x
len = 1
while x != 0:
    x = int(input())
    if x > max:
        max = x
        len = 1
    elif x == max:
        len += 1
print(len)
