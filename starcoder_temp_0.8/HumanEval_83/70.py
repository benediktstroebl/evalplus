
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(map(lambda i: i[0] == '1' or i[1] == '1', itertools.product(str(n), str(n)[::-1])))

