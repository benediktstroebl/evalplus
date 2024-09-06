
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if not n:
        return 1
    else:
        p = digits(int(n / 10))
        return 0 if not n % 2 else p * (n % 10)

