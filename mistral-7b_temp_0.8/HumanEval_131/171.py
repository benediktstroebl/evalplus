
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if not n:
        return 0
    result = 1
    while n > 0:
        x = n % 10
        n //= 10
        if x % 2 != 0:
            result *= x
    return result
