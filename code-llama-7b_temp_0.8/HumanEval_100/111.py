
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
    num_stones = []
    level = n
    while level >= 1:
        if level % 2 == 0:
            num_stones.append(level)
            level -= 2
        else:
            num_stones.append(level * 2 - 1)
            level -= 1
    return num_stones

