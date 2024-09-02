
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    if n == 1:
        count = 10
    elif n > 1:
        # The first digit can be 0-9
        # The last digit can be 0-9
        # The rest can be any combination of 0-9
        count = 9 * 9 * 10**(n-2)

    return count

