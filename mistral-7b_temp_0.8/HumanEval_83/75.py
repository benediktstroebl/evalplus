
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    res = 0
    for i in range(1,10):
        if i == 1:
            res += 1
        elif i == 0:
            res += 0
        else:
            res += (i-1)*9
    return res
