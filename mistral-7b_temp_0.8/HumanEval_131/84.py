
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    x = []
    while n:
        n,rem = divmod(n,10)
        x.append(rem)
    a = 0
    for i in x:
        if i % 2 != 0:
            a = i
    return a
