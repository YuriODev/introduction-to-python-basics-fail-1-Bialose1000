number = int(input("Enter a five digit number: "))

num1 = (number // 10000) + ((number // 100)%10) + ((((number)%10000)%1000)%100)%10
num2 = ((number // 1000)%100)%10 + ((number // 10)%100)%10
print(str(num1) + str(num2))