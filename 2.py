N=input('Введите размерность массива A')
A=[0]*int(N)
print('Введите',N,'элементов массива A')
for i in range (int(N)):
    A[i]=int(input())
print(A)
K=input('Введите размерность массива B')
B=[0]*int(K)
print('Введите',K,'элементов массива B')
for j in range (int(K)):
    B[j]=int(input())
print(B)
P=[]
for l in A:
    for m in B:
        if l==m:
            P.append(l)
print(P)

