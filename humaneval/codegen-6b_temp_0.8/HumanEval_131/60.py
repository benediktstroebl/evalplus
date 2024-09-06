
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = 1
    for i in range(len(str(n))):
        if int(str(n)[i]) % 2 == 1:
            digits *= int(str(n)[i])
    return digits

