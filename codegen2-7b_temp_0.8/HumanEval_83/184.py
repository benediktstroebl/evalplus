
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(1 if x.startswith(1) or x.endswith(1) else 0 for x in str(n)[1:])
