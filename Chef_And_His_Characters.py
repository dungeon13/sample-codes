n=int(input())
for i in range(n):
  s=input()
  t=0
  for j in range(0,len(s)-3):
    l=list(s[j:j+4])
    
    c=0
    h=0
    e=0
    f=0
    for k in range(4):
      if l[k]=='c':
        c+=1
      elif l[k]=='h':
        h+=1
      elif l[k]=='e':
        e+=1
      elif l[k]=='f':
        f+=1
    if c==1 and h==1 and e==1 and f==1:
      t+=1 
  
  if t>0:
    print('lovely',t)
  else:
    print('normal')
   
