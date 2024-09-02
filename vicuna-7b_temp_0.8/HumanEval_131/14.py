
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = [int(d) for d in str(n)[2:] if d.isdigit()]
    if not digits:
        return 0
    return sum(digits)
