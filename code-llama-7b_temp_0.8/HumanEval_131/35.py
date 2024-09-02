
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if n < 0:
        raise ValueError("Input must be a positive integer")

    n = str(n)
    product = 1
    for digit in n:
        if int(digit) % 2 == 1:
            product = product * int(digit)

    return product


