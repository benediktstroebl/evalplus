
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0
    if n % 2 == 0:
        return 0
    if n == 2:
        return 1
    num = 1
    result = 0
    for i in range(2, n):
        if n % i == 0:
            result += num
        num += i
    return result

@teardown
