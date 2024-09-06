
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 3
    elif n == 2:
        return 6
    else:
        return (n - 1) * 9 + 2
