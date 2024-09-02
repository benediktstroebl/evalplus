
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0

    for i in range(10):
        n_digits = format(i, '0'+str(n)+'b')
        if n_digits.startswith('1') or n_digits.endswith('1'):
            count += 1

    return count

