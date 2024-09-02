
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
    # n = 0
    # The base case is when n is 0, which means we just return an empty list
    # of length 0
    if n == 0:
        return [0]
    # n = 1
    # The recursive case is when n is 1, in this case we return [1]
    # as we have only one level with 1 stone
    return [n]
