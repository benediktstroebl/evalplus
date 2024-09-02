
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    digit = 1
    count = 0
    while n > digit:
        count = count + n - digit + 1
        digit = digit * 10
    return count

