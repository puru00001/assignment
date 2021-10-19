L=[12,35,18,9,56,24]
n=len(L)
s=sum(L)
mean=s/n
print("mean is"+str(mean))
L.sort()
if n%2==0:
    mid1=L[n//2]
    mid2=L[n//2 - 1]
    median=(mid1+mid2)/2
else:
    median=L[n//2]
print("median is"+str(median))
