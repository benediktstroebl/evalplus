
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    rows = n + 2
    result = rows * [0]
    result[0] = 1
    for i in range(1, rows):
        result[i] = result[i - 1] + i
        for j in range(1, i):
            result[i] -= result[j - 1]
    return result[n]
