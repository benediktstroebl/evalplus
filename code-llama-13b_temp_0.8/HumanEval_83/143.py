
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(
        count_if_it_starts_or_ends_with_one(k)
        for k in range(1, 10 ** n)
    )

