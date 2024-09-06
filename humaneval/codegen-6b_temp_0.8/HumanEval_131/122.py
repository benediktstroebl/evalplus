
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    nStr = str(n)
    dStr = ""
    for c in nStr:
        if int(c) % 2 == 1:
            dStr += c
    if not dStr:
        return 0
    else:
        return int(dStr)
