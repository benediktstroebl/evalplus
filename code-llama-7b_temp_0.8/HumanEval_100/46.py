
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
    if n < 1:
        return []

    # The first level has n stones
    pile = [n]

    # Now we add stones to the other levels
    for i in range(n - 1):
        if n % 2 == 0:
            # Even number of stones, we need to add an even number of stones
            # So we add the next odd number
            pile.append(pile[-1] + 2 * i + 3)
        else:
            # Odd number of stones, we need to add an odd number of stones
            # So we add the next even number
            pile.append(pile[-1] + 2 * i + 2)

    return pile

