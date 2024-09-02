
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # TODO: use reduce and/or multiplication
    # (like the below)
    # if n == 0:
    #     return n
    # else:
    #     return (n % 10) * digits(int(n/10))

    # a more efficient, but more straight-forward way
    return reduce(lambda x,y: x*y, [int(n % 10) for n in range(n, 0, -1) if n % 10 % 2 != 0])
