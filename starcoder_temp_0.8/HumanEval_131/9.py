
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 10:
        if n % 2 == 0:
            return 0
        else:
            return n
    else:
        r = n % 10
        if r % 2 == 0:
            return digits(n // 10)
        else:
            return r * digits(n // 10)
