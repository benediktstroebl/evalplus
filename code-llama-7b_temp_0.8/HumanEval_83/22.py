
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        raise ValueError('n must be positive')
    return sum(map(lambda s: starts_one_ends_helper(n, s), ('1', '2')))
