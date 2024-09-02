
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # product of odd digits
    product = 1
    # n2 is the square of n
    n2 = n ** 2
    while n2 > 0:
        digit = n2 % 10
        if digit % 2 != 0:
            product *= digit
        n2 //= 10
    return product if product > 0 else 0

