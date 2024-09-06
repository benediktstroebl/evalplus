
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
    n_str = str(n)

    output = 1
    for c in n_str[1:]:
        if int(c) % 2:
            output *= int(c)

    return output

