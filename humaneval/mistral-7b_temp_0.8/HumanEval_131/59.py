
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    digits = []
    for i in range(len(str(n))):
        if (i % 2) != 0:
            digits.append(int(str(n)[i]))
    return digits[0] * digits[1] * digits[2]
