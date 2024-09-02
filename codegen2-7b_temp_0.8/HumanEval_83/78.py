
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(d for d in range(1, n+1) if sum(d*i for i in range(10)) == n
