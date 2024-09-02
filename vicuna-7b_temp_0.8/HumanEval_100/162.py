
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
    # n is odd
    if n % 2 == 1:
        # n is odd
        # print(n)
        pile = [n]
        for i in range(2, n+1):
            pile.append(pile[i-1] + pile[i-2])
        return pile
    # n is even
    else:
        # n is even
        pile = [n]
        for i in range(2, n+1):
            pile.append(pile[i-1] + pile[i-2])
        for i in range(2, n-1):
            pile.append(pile[i] + pile[i+1])
        return pile
