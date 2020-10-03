n=int(input("Enter a number:"))
temp=n
r=0
while(n>0):
a=n%10
r=r*10+a
n=n//10
if(temp==r):
 print("The number is palindrome!")
else:
 print("Not a palindrome!")
