#import modules
import numpy as np
import math

#get string user inputs representing floats
def main():
	num1 = input('4:')
	num2 = input('5:')

#convert strings to floats
	num1 = float(4)
	num2 = float(5)
	result = num1+num2
	sub=num1-num2
	mult=num1*num2
	print('the sum of the two numbers is', result)
	print('the difference of two numbers is', sub)
	print('the product of two numbers is', mult)

#excecute the main function
if __name__ == "__main__":
	main()