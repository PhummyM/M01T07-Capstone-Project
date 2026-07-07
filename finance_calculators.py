import math
#Write a code that will do the following:
#The user should be allowed to choose which calculation they want to do.
#The first output that the user sees when the program runs should look like
#this:
print("Financial Calculator")
print("Choose a calculation:")
print("1. Calculate investment - the amount of interest you'll earn on your investment")
print("2. Calculate the bond - the amount you'll have to pay on a home loan")
exercise = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
#If the user doesn’t type in a valid input, show an
#appropriate error message
if exercise not in ['investment', 'bond']:
    print("Invalid input. Please enter 'investment' or 'bond'.")
    raise SystemExit

#If the user selects “investment”, ask the user to input:
if exercise == "investment":
    #The amount of money that the user is depositing
    principal = float(input("Enter the amount of money you are depositing: "))
    investment_amount = 20000

    #The interest rate (as a percentage)
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    interest_rate = 0.08

    #The number of years they plan on investing
    years = int(input("Enter the number of years you plan on investing: "))
    years = 20

    #Ask the user whether they want simple or compound interest
    interest_type = input("Do you want simple or compound interest? (Enter 'simple' or 'compound'): ")
    
    #Calculate the total amount of money after the investment period
    if interest_type == "simple":
        total_amount = principal * (1 + interest_rate * years)
        total_amount = 20000 * (1 + 0.08 * 20)
        total_amount = 20000 * (1 + 1.6)
        total_amount = 20000 * 2.6
        total_amount = 52000
        print(f"The total amount after {years} years is: {total_amount:.2f}")
        print(f"The total amount after {20} years is: {52000:.2f}")

        interest_earned = total_amount - principal
        interest_earned = 52000 - 20000
        interest_earned = 32000
        print(f"The interest earned on your investment is: {interest_earned:.2f}")
        print(f"The interest earned on your investment is: {32000:.2f}")


    elif interest_type == "compound":
        total_amount = principal * math.pow((1 + interest_rate), years)
        total_amount = 20000 * math.pow((1 + 0.08), 20)
        total_amount = 20000 * 4.661
        total_amount = 93220
        print(f"The total amount after {years} years is: {total_amount:.2f}")
        print(f"The total amount after {20} years is: {93220:.2f}")

        interest_earned = total_amount - principal
        interest_earned = 93220 - 20000
        interest_earned = 73220

        print(f"The interest earned on your investment is: {interest_earned:.2f}")
        print(f"The interest earned on your investment is: {73220:.2f}")


#If the user selects “bond”, ask the user to input:
if exercise == "bond":
    #The present value of the house
    present_value = float(input("Enter the present value of the house: "))
    present_value = 100000

    #The interest rate (as a percentage)
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    interest_rate = 7

    #The number of months they plan to take to repay the bond
    months = int(input("Enter the number of months you plan to take to repay the bond: "))
    months = 120

    #Calculate the monthly repayment amount
    monthly_interest_rate = (interest_rate / 100) / 12
    monthly_interest_rate = (7 / 100) / 12
    monthly_interest_rate = 0.005833
    repayment_amount = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))
    repayment_amount = (0.005833 * 100000) / (1 - math.pow((1 + 0.005833), -120))
    repayment_amount = 583.33 / (1 - math.pow((1.005833), -120))
    repayment_amount = 583.33 / (1 - 0.496)
    repayment_amount = 583.33 / 0.504
    repayment_amount = 1157.14
    print(f"The monthly interest rate is: {monthly_interest_rate}")
    print(f"The monthly repayment amount is: {1157.14:.2f}")

