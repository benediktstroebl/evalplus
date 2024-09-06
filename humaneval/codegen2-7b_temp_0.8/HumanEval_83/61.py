
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ans = 0
    for d in range(10, n + 1):
        ans += n - d + 1 - starts_with_one(d)
    return
