
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = 0
    for i in range(len(str(n))):
        if n % 2 != 0:
            digits += n // (2 ** (len(str(n)) - i - 1))
    return digits
