
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(c == 1 and (n >= 10 ** (i + 1) or n < 10 ** i) for i, c in enumerate(str(n)))

