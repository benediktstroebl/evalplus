
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base case
    if n == 1:
        return 1
    # if n is not 1, the count of n-digit positive integers that start or end with 1
    # is the sum of the counts of n-2 and n-1 digit positive integers that start or end with 1
    # by using 2 nested loops, one for n-1 and one for n-2, the count is doubled, and
    # this doubled count is the count of n-digit positive integers that start or end with 1.
    return (2 * (sum(starts_one_ends(n-1), starts_one_ends(n-2))))
