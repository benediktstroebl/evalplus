
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    result = 0
    temp = n
    while temp > 0:
        if temp % 10 % 2 != 0:
            result *= temp % 10
        temp //= 10
    return result
