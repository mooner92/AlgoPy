t = int(input())
for i in range(t):
    a = input()
    b = a.split()
    sum = float(b[0])
    for k in b:
        if k == "@":
            sum *= 3
        elif k == "%":
            sum += 5
        elif k == "#":
            sum -= 7
    print("%.02f" % float(sum))
