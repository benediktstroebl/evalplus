
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # count the number of n-digit positive integers that start with 1
    count_start_with_1 = (1 << n) - 1
    # count the number of n-digit positive integers that end with 1
    count_end_with_1 = (1 << n)
    return count_start_with_1 + count_end_with_1
