
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    return sum( (1 in str(n)[:i]) ^ (1 in str(n)[-i:]) for i in range(1, len(str(n))))
