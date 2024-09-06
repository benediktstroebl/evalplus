
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # If all digits are even, return 0
    if all(c % 2 == 0 for c in str(n)) == True:
        return 0
    
    # Get the digits of n
    digits = str(n)
    
    # Get the odd digits
    odd_digits = [digit for digit in digits if digit % 2 != 0]
    
    # Multiply the odd digits together
    result = 1
    for digit in odd_digits:
        result *= digit
    
    return result
