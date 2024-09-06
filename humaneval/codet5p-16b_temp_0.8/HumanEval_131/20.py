
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    l = list(str(n))
    if all(i == '0' for i in l): return 0
    return int(list(str(n))[-1]) * digits(int(list(str(n))[-2]))
