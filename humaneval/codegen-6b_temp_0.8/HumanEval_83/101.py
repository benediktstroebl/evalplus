
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0

    if n == 1:
        return 1

    n_ones = 10**(n-1)
    if n_ones > 1000000:
        return 0

    count = 0
    for i in range(1, n_ones):
        if str(i).startswith('1') or str(i).endswith('1'):
            count += 1

    return count

