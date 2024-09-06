
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ans = 0
    for i in range(10):
        if i == 1:
            ans += 10 ** (n - 1)
        else:
            ans += 10 ** n
    return ans
