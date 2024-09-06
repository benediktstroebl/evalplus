
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(i == 1 or i == 8 or i == 9 for i in range(10, n + 1))

