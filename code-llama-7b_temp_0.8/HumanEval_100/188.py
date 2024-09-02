
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
    # if n is even:
    #   go to the next even number
    # else:
    #   go to the next odd number
    pile = [n]
    while len(pile) <= n:
        next_level = pile[-1] + 2
        if next_level <= n:
            pile.append(next_level)
        else:
            pile.append(n)
    return pile
