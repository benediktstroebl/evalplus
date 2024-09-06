
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(1 if s==1 or e==1 else 0 for s, e in zip(starts_ends(n), starts_ends(n-1)))
