
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # The number of n-digit positive integers is 9^n.
    # To count the number of n-digit positive integers that start or end with 1,
    # we need to divide this number by the number of n-digit positive integers that
    # start with 1 (excluding 1 itself).
    # This is achieved by subtracting the number of n-digit positive integers that
    # start with 1 (excluding 1 itself) from 9^n.
    return (9 ** n) // (9 ** (n - 1) - (n // 2) * 9 ** (n - 2))
