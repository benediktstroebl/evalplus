
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if not isinstance(n, int) or n <= 0:
        return -1
    elif n == 1:
        return 2

    count = 0
    for i in range(1, 10 ** (n - 1)):
        if i % 10 == 1 or (i // 10) % 10 == 1:
            count += 1
    return count

