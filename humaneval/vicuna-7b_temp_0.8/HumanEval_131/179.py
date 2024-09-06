
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check for even number
    if n % 2 == 0:
        return 0
    
    # Create list of digits
    digits = [int(n % 10) for n in str(n)]
    
    # Iterate through digits
    for i in range(1, len(digits)):
        # Check for odd digits
        if digits[0] % 2 != 0 or digits[1] % 2 != 0:
            # Multiply digits and update product
            product = digits[0] * digits[1]
            for j in range(2, len(digits)):
                product *= digits[j]
            # Return product
            return product
    # All digits even, return 0
    return 0
