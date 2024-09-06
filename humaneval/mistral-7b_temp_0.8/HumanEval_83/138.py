
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    while n >= 10:
        count += n // 100
        n //= 100
    if n > 1:
        count += 1
    return count
