
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(1 for i in range(n) for j in range(n) if 10**(i-1) <= j <= 10**i and (str(j)[0] == '1' or str(j)[-1] == '1'))

