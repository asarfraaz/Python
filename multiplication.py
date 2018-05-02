multiple = input("Enter the multiple : ");
multiple=int(multiple)
range = input("Enter the Range:");
range = int(range)
count=1
while range>0:
	print(multiple,"*",count,"=",multiple*count);
	count+=1;
	range-=1;

