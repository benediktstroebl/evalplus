
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return len([n for n in range(10**(n - 1), 10**(n + 1) - 1) if n[0] == 1 or n[-1] == 1
