def mm(a, b):
    c = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            s = 0
            for k in range(3):
                s += a[i][k] * b[k][j]
            c[i][j] = s
    return c

def id3():
    e = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        e[i][i] = 1
    return e

def mp(a, n):
    if n == 0:
        return id3()
    if n == 1:
        return a

    h = mp(a, n//2)
    x = mm(h, h)

    if n % 2 == 0:
        return x
    else:
        return mm(x, a)
    
print("테스트케이스 입력 횟수를 입력해주세요.")
a = int(input())
for _ in range(a):
    print("3x3 행렬을 한줄씩 입력하고, 제곱할 횟수를 입력해주세요.")
    A = [[],[],[]]
    for r in range(3):
        A[r] = [x for x in map(float,input().split())]
    b = int(input())

    r = mp(A,b)
    for row in r:
        print(row)