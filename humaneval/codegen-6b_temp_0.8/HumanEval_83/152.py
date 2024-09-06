
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 10
    digit = 1
    shorter = n - 1
    total = 0
    while digit <= shorter:
        digit += 1
        total += (1 + 9 * (n - digit)) * 10 ** (n - digit) * (9 ** shorter)
        shorter -= 1
    return total

