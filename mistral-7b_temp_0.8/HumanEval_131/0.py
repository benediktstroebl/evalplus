
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    number = str(n)
    multiply = 1
    for i in number:
        if int(i) % 2 != 0:
            multiply *= int(i)
    return multiply
