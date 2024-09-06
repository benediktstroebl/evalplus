
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # If the number is 1, then 1 is the only option
    if n == 1:
        return 1

    # Otherwise, the count will be 2 less than the number of the number
    # of ways to choose the first digit as 1 and fill the rest of the spots
    # plus the number of ways to choose the last digit as 1 and fill the rest
    # of the spots
    return 2 * (10**n - 1)
