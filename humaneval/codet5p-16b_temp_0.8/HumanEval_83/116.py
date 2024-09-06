
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    assert(n >= 0)

    if n == 0:
        return 0

    if n == 1:
        return 1

    count = 0
    for i in range(1, 10):
        digit = str(i)
        if digit[0] == '1':
            count += 9 * 10 ** (n - 1)
        if digit[-1] == '1':
            count += 9 * 10 ** (n - 1)
    return count


