"""
This program gives the user a choice of two calculators.
The first calculator is an investment calculator, and
the second is a home loan repayment calculator.
"""

import os
import math

# Function and information strings.
def clear_screen():
    """Function to clear terminal."""
    os.system("clear||cls")
clear_screen()

OPENING_STRING = """
================Financial Calculators================

investment - to calculate the amount of interest you'll earn on your investment.
bond       - to calculate the amount you'll have to pay on a home loan.
"""

INPUT_PROMPT = "Enter either 'investment' or 'bond' from the menu above to proceed: "

# User chooses which calculator to use.
print(OPENING_STRING)
while True:
    user_selected = input(f"\n{INPUT_PROMPT}").lower()
    if user_selected.isalnum():
        if user_selected == "investment":
            break
        if user_selected == "bond":
            break
    print(f"\nYou Entered: '{user_selected}'. Try again.")
print("\n" + ("=" * 53))

if user_selected == "investment":
    clear_screen()
    print('=' * 53)
    # Investment calculator. Collect inputs.
    deposit = int(input("\nHow much are you depositing?\nEnter Amount (£): "))
    interest_rate = int(input("Interest Rate (%): ")) / 100
    num_years = int(input("Number of Years Invested: "))
    interest = input("\nType 'simple' for simple interest or 'compound' for compound interest: ").lower()

    # Calculate interest and results.
    if interest == 'simple':
        simple_interest = deposit *(1 + interest_rate * num_years)
        simple_int_earned = round(simple_interest - deposit)
        RESULTS = f"Simple Interest: £{round(simple_interest)} (£{simple_int_earned} interest earned)"
    elif interest == 'compound':
        compound_interest = deposit * math.pow((1 + interest_rate), num_years)
        compound_int_earned = round(compound_interest - deposit)
        RESULTS = f"Compound Interest: £{round(compound_interest)} (£{compound_int_earned} interest earned)"    
    else:
        RESULTS = "Try again. Enter 'simple' or 'compound' for results."
    
    # Generate results.
    print("\n" + ("=" * 53) + f"\n\n{RESULTS}\n")
else:
    clear_screen()
    print("=" * 53)

    # Bond Calculator.
    present_value = int(input("\nEnter Property Value (£): "))
    interest_rate = (int(input("Enter Interest Rate: ")) / 100) / 12
    num_months = int(input("Enter Months: "))

    # Calculate monthly mortgage repayment.
    monthly_repayment = (interest_rate * present_value)/(1 - (1 + interest_rate)**(-num_months))
    years = num_months / 12
    print("\n" + ("=" * 53))

    # Generate result string.
    RESULTS = f"""
Monthly Mortage Repayments: £{round(monthly_repayment)}
Interest rate calculated monthly at {round(interest_rate,6)}% over {round(years,2)} years.
    """
    print(RESULTS)
