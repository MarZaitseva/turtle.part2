figure = list(input())



import turtle
turtle.shape('turtle')




l = [(30,0),(30,90),(30,270),(30*(2**(1/2)),45),(30*(2**(1/2)),45),(30,180)]

def h1():

	turtle.left(l[1][1])
	turtle.forward(l[1][0])
	turtle.right(l[1][1])

def h2():

	turtle.left(l[2][1])
	turtle.forward(l[2][0])
	turtle.right(l[2][1])

def d1():

	turtle.left(l[4][1])
	turtle.forward(l[4][0])
	turtle.right(l[4][1])


def d2():

	turtle.left(l[3][1])
	turtle.forward(l[3][0])
	turtle.right(l[3][1])

def l1():

	turtle.forward(l[0][0])

def l2():

	turtle.left(l[5][1])
	turtle.forward(l[5][0])
	turtle.right(l[5][1])


def zero():

	l1()
	h1()
	h1()
	l2()
	h2()
	h2()

	turtle.penup()

	l1()
	l1()
	l1()

	turtle.pendown()


def one():

	h1()
	h1()

	turtle.penup()

	h2()
	l2()

	turtle.pendown()

	d2()

	turtle.penup()

	h2()
	l1()
	l1()
	h2()

	turtle.pendown()

	



def two():

	l2()
	d2()
	h1()
	l2()

	turtle.penup()

	h2()
	h2()
	l1()
	l1()
	l1()

	turtle.pendown()


def three():

	d2()
	l2()
	d2()
	l2()

	turtle.penup()

	l1()
	l1()
	l1()

	h2()
	h2()

	turtle.pendown()


def four():

	h1()
	h1()
	h2()
	l2()
	h1()

	turtle.penup()

	l1()
	l1()
	l1()

	h2()
	h2()

	turtle.pendown()


def five():

	l2()
	l1()
	h1()
	l2()
	h1()
	l1()

	turtle.penup()

	l1()
	h2()
	h2()
	l1()

	turtle.pendown()


def six():

	turtle.penup()

	h1()
	l2()

	turtle.pendown()

	l1()
	h2()
	l2()
	h1()
	d2()

	turtle.penup()

	l1()
	l1()
	l1()
	h2()
	h2()

	turtle.pendown()
	

def seven():

	turtle.penup()
	l2()

	turtle.pendown()

	h1()
	d2()
	l2()

	turtle.penup()

	h2()
	h2()
	l1()
	l1()
	l1()

	turtle.pendown()



def eight():

	h1()
	h1()
	l2()
	h2()
	l1()
	l2()
	h2()
	l1()

	turtle.penup()

	l1()
	l1()

	turtle.pendown()



def nine():

	turtle.penup()

	l2()

	turtle.pendown()

	d2()
	l2()
	h1()
	l1()
	h2()

	turtle.penup()

	h2()
	l1()
	l1()

	turtle.pendown()

# nine()

#num = open(numbers.txt)


func = [zero, one, two, three, four, five, six, seven, eight, nine]

z = [func[int(i)]() for i in figure]


'''
for i in figure:

	if i == "0":

		zero()


	if i == "1":

		one()

	if i == "2":

		two()

	if i == "3":


		three()

	if i == "4":

		four()

	if i == "5":

		five()

	if i == "6":

		six()

	if i == "7":

		seven()

	if i == "8":

		eight()

	if i == "9":

		nine()

'''
turtle.speed(0)
turtle.done()