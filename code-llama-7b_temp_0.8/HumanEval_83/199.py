
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # number of 1-digit numbers
    total = 9
    # number of 2-digit numbers with a leading 1
    total += 8
    # number of 3-digit numbers with a leading 1
    total += 7 * 9
    # number of 4-digit numbers with a leading 1
    total += 6 * 8 * 9
    # number of 5-digit numbers with a leading 1
    total += 5 * 7 * 8 * 9
    # number of 6-digit numbers with a leading 1
    total += 4 * 6 * 7 * 8 * 9
    # number of 7-digit numbers with a leading 1
    total += 3 * 5 * 6 * 7 * 8 * 9
    # number of 8-digit numbers with a leading 1
    total += 2 * 4 * 5 * 6 * 7 * 8 * 9
    # number of 9-digit numbers with a leading 1
    total += 1 * 3 * 4 * 5 * 6 * 7 * 8 * 9
    return total

