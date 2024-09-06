
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
    assert n >= 1, "You can't make a pile with less than 1 stone."
    if n == 1:
        return [1]
    pile = [n]
    while pile[0] != 1:
        # Cases when n is even
        if n % 2 == 0:
            if n == 2:
                return [2, 1]
            n = n // 2
            pile.insert(0, n)
        # Cases when n is odd
        else:
            if n == 3:
                return [3, 1]
            n = (n * 3) + 1
            pile.insert(0, n)
    return pile
