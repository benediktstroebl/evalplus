
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(1 for i in range(n - 1) if i + 1 + sum(1 for j in range(n - i - 1) if j + 1
