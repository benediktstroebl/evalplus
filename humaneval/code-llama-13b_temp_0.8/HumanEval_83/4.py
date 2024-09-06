
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        count = 10
    else:
        # count starts and ends with 1
        count += 10
        # count start with 1
        for i in range(1, 10):
            count += _count_n_digit_int(i, n-1)
        # count end with 1
        for i in range(1, 10):
            count += _count_n_digit_int(i, n-1)
    return count
