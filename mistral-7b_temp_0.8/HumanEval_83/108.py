
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # TODO: Fill in the function body.
    n = str(n)
    return len(n) - n.count('0') + n.count('1')

