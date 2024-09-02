
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    
    c = 0

    if n == 1:
        c += 1

    for x in range(1, 10**(n-1)):
        if (x % 10) == 1:
            c += 1
        if (x % 10) == 1 and (x // 10) % 10 == 1:
            c += 1
    
    return c
