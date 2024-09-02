
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start, end = 0, 0
    ones = str(n + 1)*n
    start, end = ones.count('1')-1, ones.count('1')
    return (start, end)
