
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(map(lambda x: 1 if x % 10 == 1 else 0, str(n)))

