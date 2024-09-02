
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 2

    total = 0

    for d in range(1, 10**(n-1)):
        if 10*d + 1 <= 10**n:
            total += 1

    for d in range(1, 10**(n-1)):
        if 10*d + 1 <= 10**n:
            total += 1

    return total
