
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(n):
        n_str = str(n)
        if n_str.startswith('1') or n_str.endswith('1'):
            count += 1
        n -= 1
    return count

