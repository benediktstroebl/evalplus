
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if all(d in (0,1) for d in str(n)):
        return 0
    
    # Otherwise, compute and return the product of the odd digits
    product = 1
    for d in str(n):
        if d % 2 != 0:
            product *= d
    
    return product
