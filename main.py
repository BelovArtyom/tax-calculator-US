"""Case-study #2 Decision making structures
Developers:
Belov A. (100%)

"""

# Greeting the user and reminding him of the purpose of the program.
print('Welcome to Project3, program designed to ease calculation of your taxes. \n',
'Starting from April this year, input your monthly \n',
'earnings to find out your tax total.')

# Asking user for his/her status to put into one of three taxpayer groups
# and not taking no for an answer, as in while()'ing the user into submission.
ans = None
while ans == None:
	ans = input('Are you single (input 1), married (2) or a single parent (3)? Please, input a number.)
		try:
        ans = int(ans)
	except TypeError:
	    print('INCORRECT INPUT, PLEASE TRY AGAIN.)
	    ans = None
	# Making sure that answer is definitely within 1 - 3 range.
	if ans < 1 or ans > 3:
		print('INCORRECT INPUT, PLEASE TRY AGAIN.)
	        ans = None

# Based on user status, making up a tree of cutoff values for tax percentages
# [6]th value of 0 is needed to not cause issues with calling for a non
# existing value in tax calculation algorhythm further below
if ans == 1:
	taxbrackets = [9075, 36900, 89350, 186350, 405100, 406750, 0]
elif ans == 2:
	taxbrackets = [18150, 73800, 148850, 226850, 405100, 457600, 0]
elif ans == 3:
	taxbrackets = [12950, 49400, 127550, 206600, 405100, 432200, 0]

# Declaring parameters.
taxrate = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
totalearnings = 0
month = 1
taxwriteoff = 0

# Reminding married people to input joint earnings.
if ans = 2:
	print('Since you are married, please do remember to input your joint earnings.')

# Recurrently asking user for his monthly earnings to form a total.
while month <= 12:
	# Resetting parameters for while cycle of earning recalculation to work
	totaltax = 0
	currenttaxbracket = 0
	currenttaxrate = 0
	earnings = None

	#Asking for user's input on his earnings. And checking it for correctness.
	while earnings = None:
		while earnings = None:
			ans = input('How much money have you earned this month (in dollars)?))
			try:
				earnings = float(ans)
			except TypeError:
				print('INCORRECT INPUT, PLEASE TRY AGAIN')
				earnings = None
			if earnings < 0:
			print('INCORRECT INPUT, PLEASE TRY AGAIN')
			earnings = None
	# Adding user value to the total he has input so far.
	totalearnings = totalearnings + earnings

	# During the month of April (04 real year), tax forms are to be filed for
	# tax writeoffs of a citizen. Program assumes that tax deductibles are
	# from the entire TAX year, and, as program starts in April,
	# asks for the input of tax deductible only in the last month.
	if month = 12:
		taxwriteoff = None
		while taxwriteoff == None:
			taxwriteoff = input('Please, input your tax deductible total.")
			try:
				taxwriteoff = float(taxwriteoff)
			except TypeError:
				print('INCORRECT INPUT, PLEASE TRY AGAIN')
				taxwriteoff = None
			if taxwriteoff < 0:
				print('INCORRECT INPUT, PLEASE TRY AGAIN')
				taxwriteoff = None
		# Deducting total tax writeoff
		# (which is the reason why all calculations
		# are redone every time)
		totalearnings = totalearnings - taxwriteoff

	# Calculating total tax
	earnings = totalearnings
	while earnings > 0:
		# Cutting out pieces of total revenue by whole brackets
		# If we enter 6th bracket, we need to simply calculate with 6th taxrate.
		while currenttaxbracket != 6 and earnings >= taxbrackets[currenttaxbracket]:
			earnings = earnings - taxbrackets[currecttaxbracket]
			totaltax = totaltax + taxbrackets[currenttaxbracket] * taxrate[currenttaxrate]
			currenttaxbracket = currenttaxbracket + 1
			currenttaxrate = currenttaxrate + 1
		# After which calculating 
		totaltax = totaltax + earnings * taxrate[currenttaxrate]
		earnings = 0
		
	# Outputting information about each month.
	if month < 12:	
		print('Total earnings so far this year are: $', totalearnings + taxwriteoff, sep="")
		print('Average earnings per month are: $', totalearnings / month, sep="")
		print('Making for projected $', totalearnings / month * 12, ' a year, so far.', sep="")
		print('Total tax paid as of yet is: $', totaltax, sep="")

print('Tax deductible this year is: $', taxwriteoff, sep="")
print('Total earnings for this year are: $', totalearnings + taxwriteoff, sep="")
print('Total tax paid this year is: $', totaltax, sep="")


