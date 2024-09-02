
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
    level_one = n
    if n % 2 == 0:
        level_two = n + 1
    else:
        level_two = n + 2
    levels = []
    levels.append(level_one)
    levels.append(level_two)
    return levels
