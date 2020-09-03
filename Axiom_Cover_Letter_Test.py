"""
Axiom Cover Letter Application Questions:

1) Given a string representing a Roman numeral:
- Write a function to compute the Arabic numerical equivalent.
Example:
- roman_to_arabic("MDCCLXXVI") should return 1776.


"""

import re

roman_numeral_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50,
         'C' : 100, 'D' : 500, 'M' : 1000,
         'IV' : 4, 'IX' :9, 'XL' : 40, 'XC' : 90,
         'CD': 400, 'CM' : 900}

def roman_to_arabic(numerals):

    # total variable used/initialized for arabic number
    arabic_number = 0
    """
    re.compile():
    - Used to combine regular expression pattern into
    pattern objects, which can be used for pattern matching.
    - It also helps to search a pattern again without rewriting it.
    """
    # Special characters
    specials = re.compile('IV|IX|XL|XC|CD|CM')
    # For all sepcial numbers within string, search within roman_numeral_dict
    # for specified value.
    for special in specials.findall(numerals):
        arabic_number += roman_numeral_dict[special] # Add number from dict
        numerals = numerals.replace(special, '', 1) # Remove value from input string
    return arabic_number + sum(roman_numeral_dict[n] for n in numerals) # Add remaining values using sum()

"""
2) Write a generic function:
- Compute various scenarios for the following optimization problem: 
A farmer owns X acres of land. 
She profits P1 dollars per acre of corn and P2 dollars per acre of oats. 
Her team has Y hours of labor available. 
The corn takes H1 hours of labor per acre and oats require H2 hours of labor per acre. 
Q: How many acres of each can be planted to maximize profits?
Test the function for the following cases (Write unit tests) :
a) X = 240, Y = 320, P1 = $40, P2 = $30, H1 = 2, H2 = 1
b) X = 300, Y = 380, P1 = $70, P2 = $45, H1 = 3, H2 = 1
c) X = 180, Y = 420, P1 = $65, P2 = $55, H1 = 3, H2 = 2 
"""

import pulp as p

def profit_max(X, Y, P1, P2, H1, H2):

    """
    Using pulp package,
    we will be able to calculate maximum profit based on:
     - Objective function
     - Constraints
    """

    # Create a LP Max problem
    Lp_prob = p.LpProblem('Profit Max Problem', p.LpMaximize)

    # Create problem Variables
    X1 = p.LpVariable("X1", lowBound = 0)   # Create a variable x >= 0
    X2 = p.LpVariable("X2", lowBound = 0)   # Create a variable y >= 0

    # Objective Function
    Lp_prob += P1 * X1 + P2 * X2, 'Objective Function'
    Lp_prob += X1 + X2 <= X, 'Acres of Land Constraint'
    Lp_prob += H1*X1 + H2*X2 <= Y, 'Hours Worked Constraint'

    # # Constraints:
    # Lp_prob += 2 * x + 3 * y >= 12
    # Lp_prob += -x + y <= 3
    # Lp_prob += x >= 4
    # Lp_prob += y <= 3


    # Display the problem
    print(Lp_prob)
    status = Lp_prob.solve()   # Solver
    print(p.LpStatus[status])   # The solution status

    # Write string for values:
    print(str(p.value(X1)) + ' acres of corn should be planted to maximize profits.')
    print(str(p.value(X2)) + ' acres of oats should be planted to maximize profits.')
    print('Maximum Profit Available: $' + str( "{:.2f}".format(p.value(Lp_prob.objective))))

    # Return values if needed for further data manipulation:
    return p.value(X1), p.value(X2), p.value(Lp_prob.objective)


""" 
3) Given the differential equation f'(x) = x^x:
- Write a function that uses Euler's method to approximate the value of f(x1),
given an initial condition (x0, f(x0)) and the value of x1.
"""

def eulers_formula(x0, x1, f_x0, h):

    # Formula:
    f_x1 = f_x0 + h * (x0^x0)
    # Return both values as (x,y) point:
    return x1, f_x1

##########################################################################################

# NOTE:
# - Had some help using StackOverflow, and originally coded inside Jupyter Notebook before
# running all my tests.

##########################################################################################
