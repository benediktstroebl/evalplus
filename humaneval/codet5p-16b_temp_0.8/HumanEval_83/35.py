
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    start_1 = 1
    count = 0
    while start_1 < n:
        count += (start_1 - 1) * (10**(start_1-1) - 10**(start_1-2))
        start_1 += 1
    return count + n - start_1
