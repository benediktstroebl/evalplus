
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum([starts_one_or_ends_one(n, i)
                for i in range(0, 10)])
