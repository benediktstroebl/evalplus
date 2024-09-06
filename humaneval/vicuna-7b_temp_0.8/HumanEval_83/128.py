
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return (sum(starts_one_ends(n//2)) + starts_one_ends(n//2)) % 2
    else:
        return (sum(starts_one_ends(n//2)) + starts_one_ends(n//2)) % 2
