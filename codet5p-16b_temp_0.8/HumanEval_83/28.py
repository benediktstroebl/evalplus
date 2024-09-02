
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    nums = [1] + [i for i in range(1, n) if i % 2 == 1]
    count = len([i for i in range(1, n + 1) if str(i).startswith("1") or str(i).endswith("1")])
    return count
