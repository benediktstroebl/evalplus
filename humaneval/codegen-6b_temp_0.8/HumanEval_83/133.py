
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start_one = cnt = 0
    for i in range(2, n+1):
        if i >= 10:
            start_one = (start_one + cnt) % MOD
        cnt = (cnt + i) % MOD

    return start_one
