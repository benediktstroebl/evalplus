
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    # if all the digits are even, then the product of odd digits is 0
    if all(digit % 2 == 0 for digit in str(n)):
        return 0

    # otherwise, multiply the odd digits
    else:
        return int(str(n).translate({ord(d): 0 for d in '02468'}).strip('0'))
