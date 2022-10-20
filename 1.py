n = int(input())
array = [float(i) for i in input().split()]

def function(c,d):
    imax = 0
    for i in range(1, c):
        if (d[i] >= d[imax]):
            imax = i
    for i in range (imax + 1, c):
        d[i] = 0
    print(d)

function(n,array)