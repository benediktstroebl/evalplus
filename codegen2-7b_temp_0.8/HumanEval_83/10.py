
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return int(
        "".join(
            [str(n // 10 ** i) for i in range(len(str(n))) if n % 10 ** i == 1]
        )
