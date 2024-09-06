
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # if n < 10:
    #     return n
    # else:
    #     return int(n % 10) * digits(int(n / 10))

    # (or)
    n = str(n)
    return int(n[:-1][1::2]) if n[0] != "0" else 0

