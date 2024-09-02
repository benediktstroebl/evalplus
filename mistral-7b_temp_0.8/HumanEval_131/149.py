
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    d = str(n)
    # print(d)
    prod = 1
    for i in d:
        if int(i) % 2 == 1:
            prod = prod * int(i)
    if prod == 1:
        return 0
    else:
        return prod

