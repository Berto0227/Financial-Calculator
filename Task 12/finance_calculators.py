#Task 12
#Bond and Investment calculator
#Programmer: Berto Swanepoel
#This program will help anyone to calculate investment as well as calculate you monthly installment when wanting to buy a house.

import math

#This part is where you ask the user to make decision, I have also explained to the user what the meaning of both words are.
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("investment     - to calculate the amount of interest you'll earn on interest.")
print("bond           - to calculate the amount you'll have to pay on a home loan.")

#The user's decision in stored in a variable call choice as this is he's or her's choice. It does not matter how the user enters the word as
#it will automatically be changed to lowercase.
choice = str(input("Please enter one of the following: (invest or bond) : ")).lower()

#This is a veriable with no input or value for now, it will be used later in the program.
interest_type = ""

#If the user's decision is invest the ask the following information.
#How much do they want to use as a starting deposit.
#What is the investment rate that the bank is offering them. This must be entered without the decimal.
#Then the user must enter the amount of year's they wish do have this investment.
#Once we have that information we need to know how the investment will be structured, nl: simple or compound.
#Lastly the investment rate is devided by 100 to get the decimal value needed for calculations.
if choice == "invest":
        deposit = float(input("Please enter the your deposit amount: "))
        i_rate = float(input("Please enter the interest rate: (Only enter the number): "))
        years = float(input("Please enter the amount of years that you'll be investing: "))
        interest_type = str(input("Please choose between 'simple' or 'compound' interest: (simple or compound) : ")).lower()
        i_r = float(i_rate /100)

#If the user has chosen the bond option, we will be needing some information so we will have to ask the user.
#We will need to know what is the value of the house, or what is the loan amount.
#What is the interest rate that the user is getting from the bank per year.
#How many months will the user be needing to pay of the house bond.
#Interest rate is now devided by 12 to get a monthly interest rate value.
#Once all that information has been given the calculation can be made.
#Now we print our the result along with a little sentance stating the monthly installment based on user's information.
elif choice == "bond":
        house = float(input("Please enter the current value of the house: "))
        b_rate = float(input("Please enter the interest rate only enter the number: "))
        months = float(input("Please enter the number of months you would to repay: "))
        b_r = float(b_rate / 12)
        repayment = house * ((b_r * (1 + b_r) ** months )/(((1 + b_r) ** months ) - 1))
        print("Your monthly installment will be R " + str(repayment))

#This to to make sure that user enters either invest or bond, in the case where user does not anything the program will stop and prompt the
#that they have not entered anything.
if not choice.isalpha():
        print ("You haven’t entered anything, please try again.")

#If user chose invest at the beginning and then also chose simple investment, the information from all the questions will then used in the
#calcuations below. The result will be printed.    
elif interest_type == "simple":
        interest =(deposit * (1 + i_r * years))
        print("Your total interest earned with " + interest_type + " will be, R " + str(interest))

#If user chose invest at the beginning and then also chose compound investment, the information from all the questions will then used in the
#calcuations below. The result will be printed.
elif interest_type == "compound":
        interest = (deposit * math.pow ((1+i_r),(years*1)))
        print("Your total interest earned with " + interest_type + " will be, R " + str(interest))





            





                      
                              



