
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 2

    start_one_count = 1
    end_one_count = 1
    for i in range(n - 2):
        start_one_count = start_one_count * 2
        end_one_count = end_one_count * 2

    return start_one_count + end_one_count
