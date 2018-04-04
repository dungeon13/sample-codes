def val(x,w,b):
    n=w*x+b
    return int(n)
t=int(input())
for i in range(t):
    n,minx,maxx=input().split()
    n=int(n)
    maxx=int(maxx)
    minx=int(minx)
    warr=[]
    barr=[]
    non=0
    spa=0
    for a in range(n):
        w,b=input().split()
        w=int(w)
        b=int(b)
        warr.append(w)
        barr.append(b)
    
        
    for j in range(minx,maxx+1):
        r=int(j)
        for k in range(n):
             r=val(r,warr[k],barr[k])
        if r%2==0:
            non=non+1
        else:
            spa=spa+1    
    print(non,spa)                  
            
      



