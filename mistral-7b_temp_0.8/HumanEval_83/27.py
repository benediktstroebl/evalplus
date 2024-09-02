
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n is 1-digit
    if n == 1:
        return 1
    # n is 2-digit
    elif n == 2:
        return 2
    # n is 3+
    else:
        return 9 * starts_one_ends(n - 1) + starts_one_ends(n - 2)

