
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    assert 1 <= n <= 9
    count = 0
    # start with ones
    for i in range(10 ** (n - 1)):
        count += 1
    # end with ones
    for i in range(10 ** (n - 1)):
        count += 1
    return count

