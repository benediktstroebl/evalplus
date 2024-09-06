
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Base case: n is 1 or 2
    if n == 1 or n == 2:
        return 1
    # If n > 2, count the number of n-digit positive integers that end with 1
    # and subtract it from the count of n-digit positive integers that start with 1
    return (sum(starts_one_ends(n//i) for i in range(1, n+1)) +
            starts_one_ends(n-1))