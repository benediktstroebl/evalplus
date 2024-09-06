
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    res = 0
    while n:
        d = n % 10
        if d == 1:
            res += n + 1
        n //= 10
    return res


