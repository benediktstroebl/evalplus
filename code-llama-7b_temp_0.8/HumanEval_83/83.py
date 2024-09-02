
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # 1 digit numbers that start and end with 1
    a = 1

    # 2 digit numbers that start with 1 and end with 1
    b = 1

    # 2 digit numbers that start with 1 and end with 1, but exclude 11
    c = 1

    # 3 digit numbers that start with 1 and end with 1
    d = 1

    # 4 digit numbers that start with 1 and end with 1
    e = 1

    # 5 digit numbers that start with 1 and end with 1
    f = 1

    for i in range(2, n):
        a += i
        b += a - c
        c += a - 1
        d += b - c
        e += b - c
        f += d - e

    return f
