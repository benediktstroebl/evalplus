
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # i.e. 11, 21, 12, 10, 31, 13, 123, 311, 111...
    i = 0
    count = 0
    while n > 0:
        d = n % 10
        n //= 10
        if d == 1:
            count += (2**i)
        i += 1
    return count

