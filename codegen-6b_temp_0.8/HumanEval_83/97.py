
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    # If n-1 digits, there are only two ways to partition: 11, 12 or 13
    # with a 1 at the end, or 2 ways with a leading 1, followed by one
    # with a leading 1.
    return starts_one_ends(n-1) + (n-1) * starts_one_ends(n-2)
