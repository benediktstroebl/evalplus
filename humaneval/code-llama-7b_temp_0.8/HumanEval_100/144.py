
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
    # Result list
    pile = []
    # Init the first level with n stones
    pile.append(n)
    # While we don't have all the levels
    while pile[-1] != 1:
        # Check if the last level is odd or even
        if pile[-1] % 2 == 0:
            # If it's even, the next level has n-1 stones
            pile.append(pile[-1]-1)
        else:
            # If it's odd, the next level has n+1 stones
            pile.append(pile[-1]+1)

    return pile
