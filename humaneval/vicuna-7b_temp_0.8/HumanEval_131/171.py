
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if n % 2 == 0:
        return 0
    
    # else, check if there is an odd digit
    d = n // 2
    while d > 0:
        if d % 2 != 0:
            return d * d
        d = d // 2
    
    # if there is no odd digit, return 0
    return 0
