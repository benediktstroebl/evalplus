
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    a_units = a % 10
    a_tens = (a % 100 - a_units) / 10
    a_hundreds = (a % 1000 - a_tens * 10 - a_units) / 100
    a_thousands = (a - a_hundreds * 100 - a_tens * 10 - a_units) / 1000
    
    b_units = b % 10
    b_tens = (b % 100 - b_units) / 10
    b_hundreds = (b % 1000 - b_tens * 10 - b_units) / 100
    b_thousands = (b - b_hundreds * 100 - b_tens * 10 - b_units) / 1000
    
    return a_units * b_units + a_tens * b_tens + a_hundreds * b_hundreds + a_thousands * b_thousands
