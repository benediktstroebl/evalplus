
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if (n <= 0):
        return 0
    if (n == 1):
        return 1
    count = 0
    for i in range(1, n):
        if (starts_one_ends(i) > 0):
            count += 1
    return count
