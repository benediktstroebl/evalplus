
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    dp = 0
    if n <= 1:
        return 1
    if n == 2:
        return 1
    for i in range(2, n+1):
        if i % 2 == 0:
            dp += i
        else:
            dp += i - 1
    return dp
