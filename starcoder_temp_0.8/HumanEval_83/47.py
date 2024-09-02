
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(
        is_equal(n, digits)
        for digits in product(range(10), repeat=n)
    )

