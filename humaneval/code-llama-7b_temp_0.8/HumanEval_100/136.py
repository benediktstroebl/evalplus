
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
    # lvl_stones = 1
    # # if n is odd, next level has one more stone
    # if n % 2 == 1:
    #     lvl_stones += 1
    #
    # pile = [lvl_stones]
    # # for each level after the first one:
    # for _ in range(n - 1):
    #     # double the number of stones if the previous level was even
    #     if pile[-1] % 2 == 0:
    #         pile.append(pile[-1] * 2 + 1)
    #     # else triple the number of stones
    #     else:
    #         pile.append(pile[-1] * 3)
    # return pile

    pile = [n]
    for i in range(n-1):
        if pile[i] % 2 == 0:
            pile.append(pile[i] * 2 + 1)
        else:
            pile.append(pile[i] * 3)
    return pile

