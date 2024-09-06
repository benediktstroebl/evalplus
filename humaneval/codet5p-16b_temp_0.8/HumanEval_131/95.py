
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    digits = 1
    for x in str(n):
        if int(x) % 2 == 0:
            digits = 0
            break
        else:
            digits = int(digits) * int(x)
    return digits
