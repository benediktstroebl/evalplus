
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # special case 1
    if n == 1:
        return 9

    # general case
    num_ends_1 = 1
    num_starts_1 = 9

    for i in range(2, n):
        num_starts_1 *= 10 - 1
        num_ends_1 *= 10 + 1

    return num_starts_1 + num_ends_1
