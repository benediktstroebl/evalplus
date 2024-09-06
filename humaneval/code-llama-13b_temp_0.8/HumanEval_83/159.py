
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        result = 4
        for i in range(3, n+1):
            result += 9 * 2 * 10 ** (i-2)
        return result
