import numpy as np
import matplotlib.pyplot as plt

def normalize(v):
    n = np.sqrt(np.sum(v*v))
    return v/n if n!=0 else v

def gram_schmidt(V):
    Q=[]
    for v in V.T:
        for q in Q:
            v -= np.dot(q,v)*q
        v = normalize(v)
        Q.append(v)
    return np.array(Q).T

def power_iteration_sym(B, iters=2000, tol=1e-9):
    b = np.random.rand(B.shape[0])
    b = normalize(b)
    for _ in range(iters):
        b_next = B @ b
        b_next = normalize(b_next)
        if np.sqrt(np.sum((b_next-b)**2)) < tol:
            break
        b = b_next
    lam = np.dot(b, B @ b)
    return lam, b

def top_k_eigen(B, k):
    Bc = B.copy()
    vals, vecs = [], []
    for _ in range(k):
        lam, v = power_iteration_sym(Bc)
        vals.append(lam)
        vecs.append(v)
        Bc -= lam * np.outer(v, v)
        Vtemp = gram_schmidt(np.array(vecs).T)
        vecs = [Vtemp[:,i] for i in range(Vtemp.shape[1])]
    return np.array(vals), np.array(vecs).T

def truncated_svd(A, k):
    B = A.T @ A
    vals, V = top_k_eigen(B, k)
    sigmas = np.sqrt(np.clip(vals,0,None))
    U = np.zeros((A.shape[0],k))
    for i in range(k):
        if sigmas[i]>1e-8:
            U[:,i] = (A @ V[:,i]) / sigmas[i]
    return U, sigmas, V

def compress_image(path, k):
    img = plt.imread(path)
    if img.ndim==3:
        img = 0.299*img[:,:,0] + 0.587*img[:,:,1] + 0.114*img[:,:,2]
    if img.max()<=1: img*=255
    A = img.astype(float)

    U,S,V = truncated_svd(A,k)
    Ak = (U*S)@V.T
    Ak = np.clip(Ak,0,255)
    err = np.sqrt(np.sum((A-Ak)**2))

    
    
    
    
    print(f"Reconstruction Error : {err:.2f}\n")

   
    plt.imshow(Ak.astype(np.uint8), cmap='gray', vmin=0, vmax=255)
    plt.title(f"Reconstructed Image (k={k})")
    plt.axis('off')
    plt.show()

if __name__=="__main__":
    fname = input("Enter image file name: ").strip()
    k = int(input("Enter k: "))
    compress_image(fname,k)
