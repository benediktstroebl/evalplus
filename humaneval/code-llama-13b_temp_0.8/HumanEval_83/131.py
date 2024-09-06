
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        raise ValueError("N must be positive")

    counts = [0, 0, 0]
    for i in range(1, 10 ** (n - 1)):
        for j in [1, 10 * (n - 1) + 1]:
            s = str(i * j)
            if s[0] == "1" or s[-1] == "1":
                counts[j - 1] += 1
    return counts

