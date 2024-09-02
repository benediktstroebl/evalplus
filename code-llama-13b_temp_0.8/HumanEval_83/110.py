
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if not n:
        raise ValueError("expected positive number, got {}".format(n))

    count = 0
    for digit in range(n):
        count += (
            4 * (10 ** digit)  # numbers that end with 1
            + (10 ** n - 10 ** (n - 1))  # numbers that start with 1
        )

    return count

