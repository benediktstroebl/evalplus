
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for num in range(1, n + 1):
        start = num // 10 ** (n - 1)
        end = num % 10
        if start == 1 or end == 1:
            count += 1
    return count

