
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
    # if n == 1:
    #     return [1]
    # elif n == 2:
    #     return [2, 1]
    # else:
    #     pile = [n, n + 1]
    #     while pile[-1] < n * 2:
    #         pile.append(pile[-1] + 2)
    #     return pile
    return [x for x in range(n, 0, -2)][::-1] + [x for x in range(n + 1, 0, -2)][::-1]

