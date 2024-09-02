
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    ans = 1
    for i in xrange(n, 1, -1):
        if i == 2:
            ans += 1
        elif i % 2:
            ans += (i // 2)
        else:
            ans += (i // 2) * 2
    return ans
