
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for x in range(10 ** (n-1), 10 ** n):
        if str(x).startswith("1") or str(x).endswith("1"):
            count += 1
    return count

