
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if sum(str(d) for d in str(n)) % 2 == 0:
        return 0
    
    # Otherwise, return the product of the odd digits
    digits = [d for d in str(n)]
    digits.reverse()
    prod = 1
    for d in digits:
        if d % 2 == 1:
            prod *= d
    return prod
