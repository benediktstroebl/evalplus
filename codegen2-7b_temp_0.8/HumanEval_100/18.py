
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
    n = abs(n)
    pile = [n]
    if n % 2 == 1:
        next_pile = [2 * n + 1]
        while next_pile:
            next_pile = [2 * n + 1 + i for i in next_pile]
            pile = pile + next_pile
    else:
        next_pile = [n + 1]
        while next_pile:
            next_pile = [n + 1 + i for i in next_pile]
            pile = pile + next_pile
    return
