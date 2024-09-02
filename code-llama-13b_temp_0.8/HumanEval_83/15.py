
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if not isinstance(n, int) or n <= 0:
        return -1

    start_one_count = end_one_count = 0
    if n == 1:
        start_one_count = 1
        end_one_count = 1
    elif n == 2:
        start_one_count = 1
        end_one_count = 2
    else:
        start_one_count = 1
        end_one_count = 2
        for i in range(3, n):
            end_one_count += 8 * 10 ** (i - 2)
    return start_one_count + end_one_count
