
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # base case: n == 0
    if n == 0:
        return 0
    
    # check if any digit is odd
    for i in range(len(str(n))):
        if n % 10 != 0 and n % 10 == i+1:
            return n / 10
    return 0
