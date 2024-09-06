
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    total = 0

    for d in range(1, 10):
        for m in range(10**(n-1), 10**n):
            if str(m).startswith(str(d)) or str(m).endswith(str(d)):
                total += 1
    return total

