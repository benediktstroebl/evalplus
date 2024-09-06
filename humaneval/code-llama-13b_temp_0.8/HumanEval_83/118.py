
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1

    total = 0
    for d in range(10):
        # For each digit, first count the numbers that start with that digit,
        # then count the numbers that end with that digit
        # then add 1 for numbers starting with 1
        total += pow(10, n - 2) * 2 + 1

    return total

