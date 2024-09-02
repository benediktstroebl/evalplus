
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # the number of three-digit numbers that start or end with 1
    count_three = n - 2

    # the number of two-digit numbers that start or end with 1
    count_two = 2 * (n - 1)

    return count_two + count_three

