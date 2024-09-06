
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
    if n <= 0:
        raise ValueError('n must be a positive integer')
    if n == 1:
        return [n]
    pile = make_a_pile(n-1)
    next_level = []
    for i, stone in enumerate(pile):
        next_level.append(stone)
        if i % 2:
            next_level.append(stone + 1)
        else:
            next_level.append(stone + 2)
    return next_
