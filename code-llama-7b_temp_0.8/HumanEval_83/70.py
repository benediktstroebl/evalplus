
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    total = 0
    for i in range(10**(n-1), 10**n):
        if str(i) == str(i).lstrip('1') or str(i) == str(i).rstrip('1'):
            total += 1
    return total

