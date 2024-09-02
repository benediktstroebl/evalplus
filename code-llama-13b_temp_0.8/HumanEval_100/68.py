
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

    pile = [1]

    while pile[-1] < n:
        # keep doubling until we are larger than or equal to n
        pile.append(pile[-1] * 2)
        if pile[-1] >= n:
            break
        # add an additional stone in case we are not exactly n
        pile.append(pile[-1] + 1)
        # cut off the last added number if it is too large
        if pile[-1] > n:
            pile.pop()

    return pile

