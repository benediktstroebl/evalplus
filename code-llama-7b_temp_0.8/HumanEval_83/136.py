
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    one_count = 0
    # get the number of 1's in binary representation
    ones_bin = bin(n).count('1')
    # if number of 1's is even, it ends with 1
    if ones_bin % 2 == 0:
        # one_count = (n - 1)
        one_count = (n * 2 - 1)
    else:
        # one_count = (n - 1)
        one_count = n * 2
    return one_count
