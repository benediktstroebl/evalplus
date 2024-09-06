
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t = 10 ** (n-1)
    return (t * 9 - t) + (t * 9 - t) // 10

