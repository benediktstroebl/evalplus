
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    total = 0

    for i in range(1, n + 1):
        count = 0
        for j in range(10**(n-1), 10**n):
            if str(j).startswith('1') or str(j).endswith('1'):
                count += 1

        total += count

    return total
