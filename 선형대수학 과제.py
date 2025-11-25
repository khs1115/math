def gauss(A):
    for c in range(3):
        pivot_row = c
        pivot_val = abs(A[c][c])
        for row in range(c+1, 3):
            if abs(A[row][c]) > pivot_val:
                pivot_val = abs(A[row][c])
                pivot_row = row

        if pivot_val < 1e-10:  
            continue

        pivot = A[pivot_row][c]
        n = pivot_row

        A[c],A[n]=A[n],A[c]
        A[c]=[num/pivot for num in A[c]]
        
        for row in range(3):
            if row!=c and abs(A[row][c]) > 1e-10:  
                k=A[row][c]
                for j in range(4):
                    A[row][j]-=k*A[c][j]

    rank_A = 0
    for r in range(3):
        if any(abs(A[r][c]) > 1e-10 for c in range(3)):  
            rank_A += 1

    rank_A_aug = 0
    for r in range(3):
        if any(abs(A[r][c]) > 1e-10 for c in range(4)):  
            rank_A_aug += 1

    if rank_A < rank_A_aug:
        print("해가 없습니다")
        return False
    
    if rank_A < 3:
        print("무수히 많은 해를 가집니다.")
        pivot_cols = []
        for r in range(3):
            for c in range(3):
                if abs(A[r][c]) > 1e-10:  
                    pivot_cols.append(c)
                    break
        
        free_cols = [i for i in range(3) if i not in pivot_cols]
        ans = ['0'] * 3
        
        for i, f in enumerate(free_cols):
            ans[f] = chr(ord('s') + i)
        
        for row in reversed(range(len(pivot_cols))):
            col = pivot_cols[row]
            expression = str(A[row][3])
            
            for f in free_cols:
                coeff = A[row][f]
                if abs(coeff) > 1e-10: 
                    term = f"{abs(coeff)}{ans[f]}"
                    if coeff > 0:
                        expression += f"-{term}"
                    else:
                        expression += f"+{term}"

            ans[col] = expression if expression != '0' else "0"
            
        print(f"x={ans[0]} y={ans[1]} z={ans[2]}")
        return True
    
    print(f"해: x={A[0][3]}, y={A[1][3]}, z={A[2][3]}")
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
        gauss(A)
       



print("테스트케이스 입력 횟수를 입력해주세요.")
a = int(input())
for _ in range(a):
    A = [[],[],[]]
    b = []
    for r in range(3):
        A[r] = [x for x in map(float,input().split())]
    b = [x for x in map(float,input().split())]

    LU(A, b)

