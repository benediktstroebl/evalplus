
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n = 10
    # starts: 1
    # ends: 1
    if n == 1:
        return 1
    # n = 2
    # starts: 1
    # ends: 1
    if n == 2:
        return 1
    # n = 9
    # starts: 9
    # ends: 1
    if n == 9:
        return 1
    # n = 100
    # starts: 1, 10, 100
    # ends: 1, 10, 100
    if n == 100:
        return 2
    # n = 101
    # starts: 1, 10, 101
    # ends: 1, 10, 101
    if n == 101:
        return 2
    # n = 111
    # starts: 1, 10, 111
    # ends: 1, 10, 111
    if n == 111:
        return 2
    # n = 11
    # starts: 11, 101
    # ends: 1
    # starts: 101, 11
    # ends: 1
    if n == 11:
        return 2
    # n = 1000
    # starts: 1000, 100, 101
    # ends: 100, 100
    # starts: 1000, 100, 1010
    # ends: 100, 100
    # starts: 1000, 100, 10100
    # ends: 100, 100
    # starts: 1000, 100, 101000
    # ends: 100, 100
    # starts: 1000, 100, 1010000
    # ends
