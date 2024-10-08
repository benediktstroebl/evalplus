
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    pos = 10**(n-1)
    for n in xrange(pos, 10**n):
        if 10**(n-1) <= n and n % 10 == 1:
            count += 1
        elif n % 10 == 1:
            count += 2
    return count
