n=int(input())
d={0:'Beginner',1:'Junior Developer',2:'Middle Developer',3:'Senior Developer',4:'Hacker',5:'Jeff Dean'}
for i in range(n):  
  e=0
  l=list(input().split(' '))
  for j in range(5):
    if l[j]=='1':
      e=e+1
  print(d[e])
      
  
   
