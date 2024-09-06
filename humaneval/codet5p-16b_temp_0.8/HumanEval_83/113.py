
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    digit = 1
    count = 0
    while digit < n:
        count += 10 ** (digit - 1) * (9 ** digit)
        digit += 1
    return count + 10 ** (digit - 1) * (9 ** digit) + 9 * (9 ** digit - 1)

