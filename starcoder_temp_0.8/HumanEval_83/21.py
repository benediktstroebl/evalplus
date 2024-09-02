
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # (111) or (1111) or (11111) etc.
    return sum(n % 10 == 1 for n in range(1, n + 1))
