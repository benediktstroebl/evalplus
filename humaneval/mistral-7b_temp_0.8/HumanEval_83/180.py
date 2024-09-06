
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # base case + recursion
    return starts_one_ends(n-1) + starts_one_ends(n-2) + starts_one_ends(n-3)

