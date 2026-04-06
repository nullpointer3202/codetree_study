#홀수이면서 3의 배수인 수
#짝수이면서 5의 배수인 수

n = int(input())

if ((n % 3 == 0)and n % 2 == 1) or ((n%5==0)and(n%2==0)) :
    print("true")
else :
    print("false")