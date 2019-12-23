# Github tuto - exercise 1

def print_message(message):
	print (message)


def print_art():
	art = """    |\\__/,|   (`
  _.|o o  |_   ) )
 -(((---(((--------
"""

	print (art)

def hi_fellow(message):
	if message == "I am an Insight Fellow!":
		print ("That's awesome! How is that random forest model going?")


if __name__ == '__main__':
	hi_fellow("I am an Insight Fellow!")

