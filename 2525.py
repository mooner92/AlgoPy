h, m = map(int, input().split())
k = int(input())
h += k // 60
m += k % 60
print((h + m // 60) % 24, m % 60)
