
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    result = 0
    for i in range(n+1):
        if n % i == 0:
            result += 1
        if n % (i+1) == 0:
            result -= 1
    return result