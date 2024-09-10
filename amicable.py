n = int(input("Enter a number:  "))
phrase = ""

def solution(n, phrase):

	sum1 = 0
	sum2 = 0

	i = 1

	while i < n:
		if n%i == 0:
			sum1 += i
			i += 1
		else:
			i += 1
	i = 1
	
	while i < sum1:
		if sum1%i == 0:
			sum2 += i
			i += 1
		else:
			i += 1
	
	if n == sum2:
		phrase = "Amicable pair!"
	else:
		phrase = "NOT an amicable pair."

	return sum1, sum2, phrase

result = solution(n, phrase)

print (result)