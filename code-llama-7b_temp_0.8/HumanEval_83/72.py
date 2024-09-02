
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    one_start = 10**(n-1)
    one_end = 10**(n-1)-1
    count = one_start+one_end
    return count

