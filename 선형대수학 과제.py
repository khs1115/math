def gauss(A):
    for c in range(3):
        pivot_row = c
        pivot_val = abs(A[c][c])
        for row in range(c+1, 3):
            if abs(A[row][c]) > pivot_val:
                pivot_val = abs(A[row][c])
                pivot_row = row

        if pivot_val == 0:
            continue

        pivot = A[pivot_row][c]
        n = pivot_row

        A[c],A[n]=A[n],A[c]
        A[c]=[num/pivot for num in A[c]]
        
        for row in range(3):
            if row!=c and A[row][c]!=0:
                k=A[row][c]
                for j in range(4):
                    A[row][j]-=k*A[c][j]

    for a in A:
        if not any(a[:3]) and a[3] != 0:
            print("해가 없습니다")
            return False

    print("무수히 많은 해를 가집니다.")
    return True


def det3(A):
    if (A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
          - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
          + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]) == 0):
              return False
          
    else:
        return True
    
def LU(A,b):
    if det3(A):
            L=[[0]*3 for _ in range(3)]
            U=[[0]*3 for _ in range(3)]
            for t in range(3):
                L[t][t]=1

            for i in range(3):
                for j in range(i, 3):
                    total = 0
                    for k in range(i):
                        total += L[i][k] * U[k][j]
                    U[i][j] = A[i][j] - total

                for j in range(i+1, 3):
                    total = 0
                    for k in range(i):
                        total += L[j][k] * U[k][i]
                    L[j][i] = (A[j][i] - total) / U[i][i]

            print("L" + "\n")
            for i in L:
                for j in i:
                    print(str(j)+" ", end="")
                print()
            
            print("U" + "\n")
            for i in U:
                for j in i:
                    print(str(j)+" ", end="")
                print()

            c1=b[0]
            c2=b[1]-L[1][0]*c1
            c3=b[2]-L[2][0]*c1-L[2][1]*c2
            y=[c1,c2,c3]

            t3=y[2]/U[2][2]
            t2=(y[1]-U[1][2]*t3)/U[1][1]
            t1=(y[0]-U[0][1]*t2-U[0][2]*t3)/U[0][0]
            
            print(f"해: x={t1}, y={t2}, z={t3}")

    else:
        A=[A[i]+[b[i]] for i in range(3)]
        if gauss(A):
            pivot_cols = []
            for r in range(3):
                for c in range(3):
                    if A[r][c] == 1 and all(A[r][k] == 0 for k in range(c)):
                        pivot_cols.append(c)
                        break
            free_cols = [i for i in range(3) if i not in pivot_cols]
            ans=[0,0,0]
            for f in free_cols:
                ans[f]=chr(ord('s')+f)
            for row in range(3):
                for col in range(3):
                    if col in pivot_cols and A[row][col]==1:
                        ex=str(A[row][3])
                        for f in free_cols:
                            if A[row][f]==1:
                                ex+=f"-{ans[f]}"
                            elif A[row][f]==-1:
                                ex+=f"+{ans[f]}"
                            elif A[row][f]==0:
                                continue
                            else:
                                ex+=f"{-A[row][f]}{ans[f]}"
                        ans[col]=ex
            print(f"x={ans[0]} y={ans[1]} z={ans[2]}")



print("테스트케이스 입력 횟수를 입력해주세요.")
a = int(input())
for _ in range(a):
    A = [[],[],[]]
    b = []
    for r in range(3):
        A[r] = [x for x in map(float,input().split())]
    b = [x for x in map(float,input().split())]

    LU(A, b)


