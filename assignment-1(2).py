y=[2,3,1,1,6,2,1,5]
y.sort()
z=len(y)
L1=[]
i=0
while i < z:
    L1.append(y.count(y[i]))
    i += 1
d1=dict(zip(y, L1))
d2={k for (k,v) in d1.items() if v == max(L1)}
print("mode is :" +str(d2))
