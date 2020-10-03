def harshadnum():
    inp=int(input('Enter number: '))
    temp=inp
    sum=0
    while (temp != 0): 
        sum = sum + int(temp % 10) 
        temp = int(temp/10) 
    if inp%sum==0:
        print('The Entered Number',inp,'is a Harshad Number')
    else:
        print('The Entered Number',inp,'is not a Harshad Number')
harshadnum()