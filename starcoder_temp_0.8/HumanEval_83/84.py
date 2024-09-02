
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    if n == 2:
        return 10

    mod = 10 ** (n - 1)
    return (9 * mod) ** 2 + (8 * mod) ** 2 + (7 * mod) ** 2 + 6 * mod * (9 * mod + 8 * mod + 7 * mod + 6)
