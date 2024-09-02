
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # A: Always start with 1
    # B: Always end with 1
    # C: Both
    # D: Neither

    # C: Only have 1s
    # D: Have 0s and/or 2s
    count = 0
    # 1000 -> 1
    for i in range(n - 1):
        # 1000 -> 10
        # 0100 -> 10
        # 0010 -> 10
        # 0001 -> 1

        # 0000 -> 0
        # 0002 -> 0
        # 0020 -> 0
        # 0200 -> 0
        # 2000 -> 0

        count += 1

    # 0001, 0010, 0100, 1000
    count += 4

    return count

