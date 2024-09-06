def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    elif n == 1:
        return 2
    else:
        # Consider the 2n possible numbers with n digits
        # Remove those that have 1 as a single digit (n possibilities)
        # Remove those that have 11 as the two first digits (1 possibility)
        return (2*n) - n - 1