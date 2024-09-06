
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    return reduce(lambda x,y: x*y, (i for i in n if i%2))

    # or
    # return reduce(lambda x,y: x*y, filter(lambda i: i%2, n))

    # or
    # return reduce(lambda x,y: x*y, filter(lambda i: i%2, str(n)))

    # or
    # return reduce(lambda x,y: x*y, (int(i) for i in str(n) if i%2))

    # or
    # return reduce(lambda x,y: x*y, (int(i) for i in str(n) if int(i)%2))

    # or
    # return reduce(lambda x,y: x*y, (int(i) for i in str(n) if int(i)%2 != 0))

    # or
    # return reduce(lambda x,y: x*y, (int(i) for i in str(n) if int(i)%2 == 0))
