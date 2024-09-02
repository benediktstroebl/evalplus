
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
    # pile = [0]
    pile = [0]
    n_stones = n
    levels = [n_stones]
    while n_stones > 0:
        level = levels.pop(0)
        stones = level
        n_stones_next = 0
        for i in range(1, n_stones + 1):
            if n_stones % i == 0:
                n_stones_next = i
                break
        stones_next = n_stones - n_stones % i
        if n_stones % 2 == 0:
            stones_next += 1
        pile.append(stones_next)
        levels.append(stones_next)
    return pile
