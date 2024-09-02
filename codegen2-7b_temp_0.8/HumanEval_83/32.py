
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum([1 for i in range(1, int(n**0.5) + 1) if i**2 == n
