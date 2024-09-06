
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    res = 0
    for i in range(1, n):
        s = str(i)
        if s[0] == "1" or s[-1] == "1":
            res += 1
    return res
