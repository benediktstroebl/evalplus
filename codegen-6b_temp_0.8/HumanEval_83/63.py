
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    assert type(n) == int and n >= 0
    res = 0
    for i in xrange(0, 10 ** n):
        digit_str = str(i)
        if digit_str[0] == '1':
            res += 1
        if digit_str[-1] == '1':
            res += 1
    return res

