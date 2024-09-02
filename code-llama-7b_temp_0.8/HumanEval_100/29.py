
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
        raise ValueError("n must be > 0")
    elif n == 1:
        return [1]
    elif n == 2:
        return [2, 2]

    pile_levels = [n]
    next_level = n + 1
    while next_level > 0:
        if next_level % 2 == 0:
            next_level -= 1
        pile_levels.append(next_level)
        next_level += 1

    return pile_levels[1:]

