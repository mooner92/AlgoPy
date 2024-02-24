t = int(input())
for i in range(t):
    a, b = map(input().split())
    for j in range(a):
        for k in range(a):
            print(b[j], end="")

    print("")
