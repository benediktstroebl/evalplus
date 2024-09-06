
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 5

    count = 0
    for i in xrange(10 ** (n - 1), 10 ** n):
        if i % 10 == 1:
            count += 2
        if i % 10 == 9:
            count += 1
    return count

