
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if not n >= 0:
        return 0
    else:
        lst = [int(i) for i in str(n)]
        if any(i % 2 == 0 for i in lst):
            return 0
        else:
            return reduce(lambda x, y: x * y, [i for i in lst if i % 2 != 0])

