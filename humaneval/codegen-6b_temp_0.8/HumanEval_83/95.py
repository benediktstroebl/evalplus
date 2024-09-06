
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    total = 0
    for i in xrange(1, n + 1):
        if str(i).startswith("1"):
            total += 1
        if str(i).endswith("1"):
            total += 1
    return total

