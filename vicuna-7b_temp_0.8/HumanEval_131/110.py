
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # check if all digits are even
    if all(c % 2 == 0 for c in str(n)):
        return 0
    else:
        # if not, return the product of the odd digits
        return int(n) % 2 == 1 and int(n / 2) % 2 == 1 and int(n / 4) % 2 == 1 and int(n / 8) % 2 == 1 and int(n / 16) % 2 == 1
