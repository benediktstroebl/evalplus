
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # count of numbers that end in 1
    num_end_with_one = 0

    # count of numbers that start in 1
    num_start_with_one = 0

    # count of numbers that start or end in 1
    num_start_end_with_one = 0

    for i in range(0, n):
        num_end_with_one += (10 ** i) * 9
        num_start_with_one += (10 ** (n - i - 1)) * 9
        num_start_end_with_one += (10 ** i) * 9

    return num_start_end_with_one - num_end_with_one - num_start_with_one
