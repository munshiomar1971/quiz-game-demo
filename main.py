# this is a simple quiz game in python
import sys
import time

# prints slowly
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)



# options menue
def options():
		print("-----------------------")
		print("-                     -")
		print("-                     -")
		print("-     Options         -")
		print("-                     -")
		print("-                     -")
		print("- By: Omar Sumon      -")
		print("-                     -")
		print("-----------------------")

		print("There are no options haha")

		quiz()



# menue (pops up when user types esc)
def menue():
		print("-----------------------")
		print("-                     -")
		print("-                     -")
		print("-     Quizlet!!!      -")
		print("-                     -")
		print("-                     -")
		print("- By: Omar Sumon      -")
		print("-                     -")
		print("-----------------------")

		slowprint("What Would you like to do?")
		print("1. Quit")
		print("2. See Options")

		menue = input("You: ")


		if menue == "1":
			slowprint("Exiting Game")
			slowprint("Good Bye")
		elif menue == "2":
			options()
		else:
			slowprint("Please Enter a valid option, quitting game now")





		
# start menue
def Startmenue():
		print("-----------------------")
		print("-   Welcome           -")
		print("- To                  -")
		print("-     Quizlet!!!      -")
		print("-                     -")
		print("-                     -")
		print("- By: Omar Sumon      -")
		print("-                     -")
		print("-----------------------")

		slowprint("What whould you like to do?")
		print("1. Start Game")
		print("2. Quit")
		start = input("You: ")

		if start == "1":
			slowprint("Starting game")
			quiz()

		elif start == "2":
			slowprint("Exiting Game")
			slowprint("Good Bye")
		else:
			slowprint("Please Enter a valid option, quitting game now")






# end screen
def endscr():
	slowprint("Game Over!")
	print("------------------------")
	print("-                      -")
	print("-     Game Over!       -")
	print("-                      -")
	print("-Thank you for playing!-")
	print("-                      -")
	print("- By: Omar Sumon       -")
	print("-                      -")
	print("------------------------")

	slowprint("Report problems at github")

	# quit logic

	if 3 < 18:
		sys.exit()
	else:
		quiz()







	

# the actual game
def quiz():
	global points

	# question 1
	slowprint("Welcome to the Quiz lets start!")
	print("What is 5 + 5?")
	answer = input("You: ")

	# logic for question 1
	if answer == "10":
		slowprint("Good job! lets see your points")
		points = "1"
		print("Points: " + points)
		slowprint("Next Question")
	elif answer == "esc":
		menue()
	else:
		slowprint("You failed! let us see your points")
		points = "-0"
		print("Points:" + points)
		slowprint("BAHAHHAHAHAHAH IMAGINE")
		slowprint("Next Question")

	# question 2
	slowprint("Question 2: ")
	print("What is 1 x 10000")
	answer = input("You: ")

	# logic for question 2
	if answer == "10000":
		slowprint("Good job! lets see your points")
		points = "2"
		print("Points: " + points)
		slowprint("Next Question")
	elif answer == "esc":
		menue()
	else:
		slowprint("You failed! lets see your points")
		points = "1"
		print("Points: " + points)
		slowprint("Next Question")

	# question 3
	slowprint("Question 3: ")
	print("What is 10 / 2? (division) ")
	answer = input("You: ")

	# logic for question 3
	if answer == "5":
		slowprint("Good job! lets see your points!")
		points = "3"
		print("Points: " + points)
		slowprint("Next Question")
	elif answer == "esc":
		menue()
	else:
		slowprint("You failed! lets see your points")
		points = "2"
		print("Points: " + points)
		slowprint("Next Question")

	quiz2()







# quiz part 2

def quiz2():
	# question 1
	slowprint("Now lets move on to harder questions")
	print("Where are you right now?")

	answer = input("You: ")

	slowprint("I can see you")
	slowprint("..............")

	# question 2
	slowprint("Next Question")
	print("How hot is the sun?")

	answer = input("You: ")

	if answer == "hot":
		slowprint("hmmm ok, lets see your points")
		points = "4"
		print("Points: " + points)
	elif answer == "5,778 k":
		slowprint("You are correct! lets see your points")
	else:
		slowprint("Moving on...")

	# question 3

	slowprint("are you alone?")

	answer = input("You: ")

	# question 3 logic

	if answer == "esc":
		slowprint("There is no escape")
	else:
		slowprint("I can see you")
		slowprint("..............")

	# question 4
	print("01001001 00100000 01101011 01101110 01101111 01110111 00100000 01110111 01101000 01100101 01110010 01100101 00100000 01111001 01101111 01110101 00100000 01100001 01110010 01100101")

	answer = input("You: ")

	slowprint("Good Bye. :)")

	endscr()













def main():
	Startmenue()

if __name__ == '__main__':
	main()