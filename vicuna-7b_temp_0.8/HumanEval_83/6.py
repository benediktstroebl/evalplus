
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # The count of n-digit positive integers that start with 1 is the count
    # of n-digit positive integers that end with 1.
    # So we can calculate the count of n-digit positive integers that start
    # with 1 by taking the reciprocal of the count of n-digit positive integers
    # that end with 1.
    return 1 / sum([bin(i)[2] for i in range(n+1) if bin(i)[2] == '1'])
