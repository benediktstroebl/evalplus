
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    result = 10 ** (n - 1) + 1
    for i in range(1, n):
        result += 10 ** i * 9 * i
    return result

