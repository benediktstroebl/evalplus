
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # 1 <= n <= 10
    s1 = 1
    for i in range(2, n):
        s1 += 9 * 10 ** (i - 1)
    s2 = 9 ** n
    return s1 + s2
