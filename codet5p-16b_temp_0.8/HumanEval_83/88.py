
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n < 1: return 0
    if n == 1: return 1
    if n == 2: return 2

    result = [1, 1]
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])
    return result[-1]
