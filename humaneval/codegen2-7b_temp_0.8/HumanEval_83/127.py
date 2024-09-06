
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(
        map(lambda n: int(str(n)[0] == str(n)[-1]), range(1, n + 1))
    )
