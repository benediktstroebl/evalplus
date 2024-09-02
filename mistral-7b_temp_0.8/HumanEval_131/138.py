
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if n < 0:
        return 0
    num = n
    product = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 1:
            product *= digit
        num //= 10
    return product







