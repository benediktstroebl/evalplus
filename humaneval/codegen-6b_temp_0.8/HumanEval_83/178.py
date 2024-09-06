
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n > 10:
        return 0
    if n == 1:
        return 9
    digits = 9
    count = 1
    while digits < n:
        count *= 10
        digits += 1
    digits = 9
    while digit < n:
        count *= 10
        digit += 1
    return count

