
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ans = 0
    for i in xrange(1, 10):
        if n == 1:
            ans += 1
        elif n == 2:
            ans += 9
        else:
            ans += (9 ** n)

    return ans
