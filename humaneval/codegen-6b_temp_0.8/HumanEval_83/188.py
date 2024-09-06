
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    result = 0
    for i in range(2, n + 1):
        if i <= 9:
            result += 1
        elif i % 10 == 1 or i % 10 == 9:
            result += 1
    return result

