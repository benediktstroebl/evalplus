
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
    stones_at_level = []
    n_stones = n
    for i in range(n):
        stones_at_level.append(n_stones)
        n_stones = n_stones + 1 if n_stones % 2 == 1 else n_stones + 2
    return stones_at_level

