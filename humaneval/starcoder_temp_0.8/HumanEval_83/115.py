
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    assert 1 <= n <= 10000
    num = int(str(9) * n) + 1
    count = 0

    for i in range(1, num):
        if i % 10 == 1 or i // (10 ** (n - 1)) % 10 == 1:
            count += 1

    return count

