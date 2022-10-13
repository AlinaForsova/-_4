N=input('Введите размерность массива')
D=[0]* int(N)
print('Введите',N,'элементов массива')
for i in range (int(N)):
    D[i]=float(input())
print(D)
K=max(D)
maxD=max(D)
number=0
for j in range(len(D)):
    if D[j]==maxD:
        number=j+1
for l in range(number,len(D)):
    D[l]=0
print(D)
