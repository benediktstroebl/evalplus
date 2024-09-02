
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    # no one likes lists and if statements
    # use recursion to find the sum of the next level
    # keep track of how many levels we've gone through
    # sum all the levels up to the current level
    sum = 0
    if n <= 1:
        return [n]
    if n % 2 == 0:
        return [n, 2*n + 1, 3*n + 2]
    else:
        return [n, 2*n + 1]

