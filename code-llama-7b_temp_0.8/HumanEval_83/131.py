
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 9

    ones = 9
    ninety_nines = 9

    for i in range(2, n):
        ones *= 10
        ones += 1
        ninety_nines *= 9

    return ones + ninety_nines

