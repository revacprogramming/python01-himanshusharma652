# Conditional Execution

hrs = input("Enter hours: ")
h = float(hrs)
rate=input("enter rate: ")

r=float(rate)
if h<=40:
    tot = h*r
    print(tot)
else:
  i = h - 40
  t1=40 * r
  t2=i*1.5*r
  t=t1+t2
  print(t)