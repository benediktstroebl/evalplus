
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # special case
    if n == 0:
        return 0

    count = 0
    for i in range(9 * (10 ** (n - 1))):
        digits = count_digits(i)
        if digits > 1 and digits == n:
            count += 1
    for i in range(9 * (10 ** (n - 1))):
        digits = count_digits(i)
        if digits > 1 and digits < n:
            count += 1

    return count

