
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    str_n = str(n)
    p = 1
    for ch in str_n:
        if int(ch) % 2 == 1:
            p *= int(ch)
    return p
