
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    if n == 1:
        count += 1
    if n == 2:
        count += 2
    if n == 3:
        count += 4
    if n >= 4:
        count += 8 + starts_one_ends(n - 1)
    return count
