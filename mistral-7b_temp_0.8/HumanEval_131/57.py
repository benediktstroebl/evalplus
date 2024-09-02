
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # return 0 if all digits are even
    if all(dig % 2 == 0 for dig in str(n)):
        return 0

    # return the product of odd digits
    return int(str(n)[::2])

