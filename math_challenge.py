import random

def main():
	ops = list('+-/*')
	nums = list('123456789')
	operator1, operator2 = list(random.sample(ops,2))
	l = []
	for op1 in ops:
		for op2 in ops:
			for num1 in nums:
				for num2 in nums:
					for num3 in nums:
						try:
							val = eval(num1+op1+num2+op2+num3)
							if round(val) == val:
								l.append(val)
						except e:
							continue
	possible = list(set(l))
		
	def question():
		while True:
			x, y, z = random.sample(nums, 3)
			val = eval(x + operator1 + y + operator2 + z)
			if operator1 == '/':
				mid_way = eval(x + operator1 + y)
				if round(mid_way) != mid_way:
					continue
			elif operator2 == '/':
				mid_way = eval(y + operator2 + z)
				if round(mid_way) != mid_way:
					continue
			if val in possible:
				res = val
				break
				
		print("Find values of a, b and c: \n\na {} b {} c = {}\t\tPress Ctrl + C to exit".format(operator1, operator2, res))
		a = input("Enter a: ")
		b = input("Enter b: ")
		c = input("Enter c: ")
		if eval(a + operator1 + b + operator2 + c) == res:
			print("Correct output!")
			print('-'*30)
		else:
			print("Incorrect!\nOne of the correct solutions: ")
			print("{} {} {} {} {} = {}".format(x,operator1,y,operator2,z,res))
			print('-'*30)
	
	while True:
		question()
	
	
	

if __name__ == '__main__':
	main()
