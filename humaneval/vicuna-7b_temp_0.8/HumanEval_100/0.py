
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
    # this is the worst case scenario, where n is odd and n-1 is even
    if n % 2 == 1:
        return [n, n-1, n-2]

    # all other cases
    return [n, n-1, n-3, n-2, n-4, n-3, n-5]
