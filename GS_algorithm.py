def qr_factor(A):
    
    m, n = np.shape(A)

    Q = np.zeros((m,n))
    R = np.zeros((n,n))
    
    for k in range(n):
        Q[:, k] = A[:, k]

        for j in range(k):
            R[j, k] = np.dot(Q[:, j], A[:, k])
            Q[:, k] -= R[j, k] * Q[:, j]

        R[k, k] = np.linalg.norm(Q[:, k], 2)
        Q[:, k] /= R[k, k]
            

    
    return Q, R
    

Q, R = qr_factor(A)
