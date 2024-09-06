
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n < 1:
        raise ValueError("n must be >= 1")

    count = 0
    for i in range(1, 10 ** (n - 1)):
        s = str(i)
        if (s[0] == '1') or (s[-1] == '1'):
            count += 1

    return count
