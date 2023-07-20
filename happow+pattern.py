n=5
k=round(n/2+1)
for i in range(1,n+1):
  for j in range(1,n+1):
    if (i==k-1 or j==k-1):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
