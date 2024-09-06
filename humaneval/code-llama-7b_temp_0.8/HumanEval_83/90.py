
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # STRIP LEADING 1s
    n -= n // 10

    # DIVIDE BY 10
    n //= 10

    # STRIP TRAILING 0s
    n -= n // 10

    # DIVIDE BY 10
    n //= 10

    # ADD 1 FOR EACH 0 THAT REMAINS AND 1 FOR THE 10s PLUS THE ONES PLUS THE 1s
    # THAT ARE LEFT
    return (1 + n) * 10 + 1


