
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start_ends = 0
    for i in range(10):
        if str(i) * (n - 1) + "1" in range(10 ** n):
            start_ends += 1
    return start
