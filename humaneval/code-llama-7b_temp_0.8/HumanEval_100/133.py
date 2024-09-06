
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
    # n must be a positive integer
    if not isinstance(n, int) or n <= 0:
        return None
    # create a list to store the number of stones in each level
    pile = []
    # add the number of stones in the first level
    pile.append(n)
    # if n is odd, the number of stones in the next level is the next odd number
    if n % 2 == 1:
        for i in range(n-1):
            pile.append(pile[i] + 2*i + 3)
    # if n is even, the number of stones in the next level is the next even number
    else:
        for i in range(n-1):
            pile.append(pile[i] + 2*i + 2)
    return pile
