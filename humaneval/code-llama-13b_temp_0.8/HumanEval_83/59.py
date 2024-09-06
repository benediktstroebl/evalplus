
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    c = 0
    for i in range(n):
        if i == 0 or i == n - 1:
            c += 1
    return c

