
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # handle the special case of a single digit number
    if n < 10:
        return n * 10

    # handle the special case of all even digits
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0

    # handle the general case
    digits = 0
    for i in range(1, len(str(n))):
        if str(n)[i] % 2 != 0:
            digits += str(n)[i]
            n = str(n)[0:i] + str(n)[i+1:]
    return digits
