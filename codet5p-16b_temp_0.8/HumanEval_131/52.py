
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    return 0 if sum(int(x) % 2 for x in str(n)) == 0 else int(''.join(str(x) for x in str(n) if int(x) % 2 == 1))
