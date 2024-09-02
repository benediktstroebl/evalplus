
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    result = 0
    for i in range(10 ** (n - 1), 10 ** n):
        d = i % 10
        if d == 0 or d == 9:
            result += 1
    return result

