
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
    # Write the function that takes in two integers and returns the product of their unit digits.
    # Use a while loop and a temporary variable to keep track of the digits.
    # To get the unit digits, divide by 10 repeatedly.
    # To add the digits, multiply them together.
    # To get the final answer, add the digits together.
    # The result should be stored in the same variable as the final product.
    # If the result is zero, return 0.
    # If the input is negative, return a negative number.
    # If the input is positive, return a positive number.
    # If the divisor is zero, return 0.
    # If the divisor is not zero, return -1.
    # If the divisor is negative, return -1.
    # If the divisor is not a power of 10, return -1.
    # If the divisor is too large, return -1.
    # If the divisor is too small, return -1.
    # If the divisor is not an integer, return -1.

    # base case: if the divisor is 0, the answer is 0
    if a == 0 or b == 0:
        return 0
    
    # if the divisor is not a power of 10, return -1
    # handle this case separately
    if not div_1(a,b):
        return -1
    
    # base case: if the divisor is 1, the answer is the last digit of the first number
    if a%1 == 0:
        return multiply(a//1, b)
    
    # if the divisor is negative, the answer is negative
    if b<0:
        return -1
    
    # if the divisor is not an integer, return -1
    if not int(b):
        return -1
    
    # convert the divisor to a string and check if it's a valid divisor
    temp_str = str(b)
    if temp_str[-1] in '0123456789':
        return -1
    else:
        return -1
