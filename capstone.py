"""
create a program that will allow the user to chose from 
to use two different fnancial calculators: an investment calculator and a home
loan repayment calculator
promt user to pick either investment or bond calculation
the code should be able to read the user input regardless of how it is typed
if an invaild input is provided dispaly appropriate error message and ask user
to try and again
"""

# ========================== IMPORTS ==========================
import math


# ========================== MAIN CODE ==========================
print("investment - to calculate the amount of intrest you'll earn\
 on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

user_input = ""

while user_input != "bond" or user_input != "investment":
    user_input = input("\nEnter either 'investment' or 'bond' from the\
 menu above to proceed: ").lower()

    if user_input == "investment":
        deposit = int(input("Enter the amount you would like to deposit: "))
        intrest_rate = int(input("Enter intrest rate: "))
        intrest_rate = intrest_rate / 100
        years_saving = int(input("How many years do want to invest: "))
        intrest = input("Do you want \"simple\" or \"comound\" \
 intrest: ").lower()

        if intrest == "simple":
            total = deposit * (1 + intrest_rate*years_saving)
            total_diff = total - deposit
            print(f"\nYour total amount of intrest is {total_diff}, your end\
 balence is {total}.")
            break

        elif intrest == "compound":
            total = deposit *  math.pow((1 + intrest_rate),years_saving)
            total = round(total,2)
            total_diff = total - deposit
            print(f"\nYour total amount of intrest is {total_diff}, your end\
 balence is {total}.")
            break

    elif user_input == "bond":
        house_value = int(input("What is the value of your house: "))
        intrest_rate = int(input("Enter intrest rate: "))
        intrest_rate = intrest_rate / 100
        months_payback = int(input("How many months do you want to pay back\
 over: "))
        repayment = (intrest_rate * house_value)/(1 - (1 + intrest_rate)**(-months_payback))
        repayment = round(repayment, 2)
        print(f"The amount you will have to pay back each month is {repayment}.")
    else:
        print("Invalid option, please choose from the options provided!")
        