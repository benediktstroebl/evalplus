
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even.
    if n % 2 == 0:
        return 0
    
    # Initialize the result to 1.
    result = 1
    
    # Loop through the digits of n.
    for i in range(1, len(str(n))):
        # If the current digit is odd, add it to the result.
        if n[i] % 2 != 0:
            result *= n[i]
    
    return result
