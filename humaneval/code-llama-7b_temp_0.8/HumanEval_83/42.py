
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return 9 * sum(map(int, str(n)[1:])) + 9 * sum(map(int, str(n)[:-1]))

