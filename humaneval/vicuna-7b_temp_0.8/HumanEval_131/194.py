
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # base case: if all digits are even, return 0
    if sum(map(bool, str(n))) == 2*len(str(n)):
        return 0
    
    # handle the case where at least one digit is odd
    digits = []
    for i in range(len(str(n))):
        if n % 2 != 0:
            digits.append(int(n % 10))
    return sum(digits)
