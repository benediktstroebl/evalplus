
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    product = 1

    while n > 0:
        n, last_digit = divmod(n, 10)
        if last_digit % 2:
            product *= last_digit

    return product

