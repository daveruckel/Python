balls = [6, 1, 4, 2, 8]

def solution(balls):

	moves = 0 # No of moves it will take (output)
	num_balls = len(balls) # find number of balls
	consec_balls = 0  # No of balls that are next to each other
	nonconsec_balls = 0 # No of balls that are not next to each other
	a = 0
	b = 0
	#diff = (b - a) + 2

	balls.sort()

	for a, b in zip(balls, balls[1:]):
		diff = (b - a) - 1  # No of gaps between each ball...diff - 1
		if diff == 0:
			consec_balls += 1
		else:
			nonconsec_balls += 1

	return(consec_balls, nonconsec_balls)

result = solution(balls)

print(result)