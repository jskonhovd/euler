#!/usr/bin/python

def fib(size):
	arr = []

	arr.append(1)
	arr.append(2)
	count = 0
	x = 0
	
	while(arr[x+1] < size):
		foo = arr[x] + arr[x+1]
		if(foo < size):
			arr.append(foo)
		else:
			break
		print(arr)
		x = x + 1
	
	for index in range(len(arr)):
		if((arr[index]) % 2 == 0):
			count = count + arr[index]
			print(arr[index])

	return count

ans = fib(4000000)
print(ans)
