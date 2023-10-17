import numpy as np
def gauss_elimination(A, B):
    n = len(B)
    
    for i in range(n-1):
        imax=np.argmax(A[i],axis=0)
        if A[i][i] == 0.0:
            tmp=A[i]
            A[i]=A[i+1]
            A[i+1]=tmp
            
        for j in range(i+1, n):
            ratio = A[j][i]/A[i][i]
            for k in range(i,n):
                A[j][k] = A[j][k] - ratio * A[i][k]
            B[j] = B[j] - ratio * B[i]
    
    
    X = np.zeros(n)
    X[n-1] = B[n-1]/A[n-1][n-1]
    for i in range(n-2, -1, -1):
        S=0
        for j in range(i+1,n):
             S= S + A[i][j] * X[j]
        X[i]=(B[i]-S)/A[i][i]
    return X

#example:
A = np.array([[2,4,-3], [2, 5, -1], [2, 1, 3]])
B = np.array([2, -1, 2])
X = gauss_elimination(A, B)
print("Solution:", X)
