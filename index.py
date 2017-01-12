t=int(raw_input())
for y in range(t):
   a=[]
   k=int(raw_input())
   for i in range(k):
      m= int(raw_input())
      a.append(m)
   x=0
   for j in range(k):
       x=(2**x)-a[j]
       if (x<0):
         break
       if (x==0):
          if (sum(a[j+1:])!=0):
            x=1
            break
          else : 
            break  
   if (x==0):
       print "Yes"
   else:
       print "No"             
thank you!!
