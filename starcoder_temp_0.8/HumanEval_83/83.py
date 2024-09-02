
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(x % 10 == 1 or x % 10 == 9 for x in range(1, n + 1))
