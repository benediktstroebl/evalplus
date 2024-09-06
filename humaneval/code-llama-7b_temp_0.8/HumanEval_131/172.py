
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
    total_product = 1
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            total_product *= digit
        n //= 10
    return total_product
