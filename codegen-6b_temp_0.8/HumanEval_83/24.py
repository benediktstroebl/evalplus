
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(str(n).startswith('1') ^ str(n).endswith('1') for n in range(1, 10**(n+1)))
