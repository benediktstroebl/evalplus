
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    x = n
    r = 0
    while x > 0:
        if x % 10 % 2 == 1:
            r = r*x%10
        x = x//10
    return r

