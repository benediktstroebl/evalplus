
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(
        1
        for num in range(n, 10 ** (n - 1), -1)
        if str(num).startswith("1") or str(num).endswith("1")
    )
