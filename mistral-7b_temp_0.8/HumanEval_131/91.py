
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    n = str(n)
    odd = 1
    for i in n:
        if int(i) % 2 != 0:
            odd *= int(i)
        else:
            continue
    if odd == 1:
        return 1
    else:
        return odd
