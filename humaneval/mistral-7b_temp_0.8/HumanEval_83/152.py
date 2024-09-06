
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    while n > 0:
        n = n - 1
        if (n % 10) == 1:
            count += 1
        n = n / 10
    return count
