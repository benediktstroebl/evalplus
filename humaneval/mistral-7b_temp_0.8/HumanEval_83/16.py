
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Base case.
    if n == 1:
        return 10
    # Recursive case.
    return starts_one_ends(n - 1) + starts_one_ends(n - 1)
