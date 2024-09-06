
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    "*** YOUR CODE HERE ***"
    num = n
    prod = 1
    while num > 0:
        if num % 2 == 1:
            prod *= num % 10
        num //= 10
    return prod
