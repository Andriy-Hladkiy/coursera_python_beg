a = int(input())
b = int(input())
n = int(input())

price = (a * 100) + b
total_price = price * n
print(total_price // 100, total_price % 100)
