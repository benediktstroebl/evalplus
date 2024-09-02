
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
    # add the first level with n stones
    pile = [n]

    # find the number of stones in the next level
    if n % 2 == 0:
        next_even = 2 * n // 2
    else:
        next_odd = 2 * n + 1
        pile.append(next_odd)

    # keep adding the next level until the pile is full
    while len(pile) < n:
        if n % 2 == 0:
            next_even = 2 * n // 2
        else:
            next_odd = 2 * n + 1
            pile.append(next_odd)

    # reverse the order of pile
    pile.reverse()

    return pile
