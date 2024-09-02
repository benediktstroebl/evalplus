
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Base cases
    if n == 1:
        return 10

    # Recursive calls
    return starts_one_ends(n - 1) * 9 + ends_one(n - 1)

