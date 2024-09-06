
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n-1 digit numbers that end with 1
    d = (n//10) + 1
    count = d*(d+1)/2
    # n-1 digit numbers that start with 1
    e = (n//10) + 1
    count += e*(e+1)/2
    return count
