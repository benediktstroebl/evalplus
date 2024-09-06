
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # The recurrence relation is given by T(n) = T(n-1) + T(n-2)
    # So we can use the closed form for n = 1
    return 2 * (n // 2 + (n // 2) // 2)
