
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    my_product = 1
    if n < 1:
        raise ValueError("Digits requires a positive integer")
    while n > 10:
        digit = n % 10
        if digit % 2 != 0:
            my_product *= digit
        n //= 10
    if n % 2 != 0:
        my_product *= n
    return my_product

