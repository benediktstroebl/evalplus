
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
    # we start with n
    pile = [n]
    # we check if n is even
    if n % 2 == 0:
        # if it is, we add the next even number
        pile.append(n + 2)
        # we repeat until we reach 0
        while pile[-1] != 0:
            # if n is even, we add the next even number
            if pile[-2] % 2 == 0:
                pile.append(pile[-2] + 2)
            # if n is odd, we add the next odd number
            else:
                pile.append(pile[-2] + 2)
        # when the last element in the list is 0, we remove it
        return pile[:-1]
    # if n is not even, we add the next odd number
    else:
        pile.append(n + 1)
        while pile[-1] != 0:
            if pile[-2] % 2 == 1:
                pile.append(pile[-2] + 2)
            else:
                pile.append(pile[-2] + 2)
        return pile[:-1]

