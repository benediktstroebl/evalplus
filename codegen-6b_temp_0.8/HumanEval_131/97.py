
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    a = n
    l = []
    while a == 0:
        l.append(a)
        a = a // 10
    for i in l:
        if i % 2 != 0:
            return i
    return 0

