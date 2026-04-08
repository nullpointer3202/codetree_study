a , b, c= map(int, input().split())

m = 0

if (a>=b and a<=c) or (a>=c and a<= b) :
    m = a
elif (b>=a and b<=c) or (b>=c and b<=a) :
    m = b
elif (c>=a and c<=b) or (c>=b and c<=a) :
    m = c
print(m)