
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0
    return sum(1 for x in range(1, 10 ** n) if x == 1 or x % 10 == 1)
