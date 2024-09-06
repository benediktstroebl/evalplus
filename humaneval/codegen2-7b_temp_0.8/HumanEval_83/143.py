
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(
        [1 if i in n_ends else 0 for i in range(10**(n-1), 10**n)])

