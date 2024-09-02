
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
    # # Solution 1
    # lst = []
    # i = n
    # while i > 0:
    #     if i % 2 == 0:
    #         lst.append(i)
    #     else:
    #         lst.append(i + 1)
    #     i -= 2
    # lst.reverse()
    # return lst

    # Solution 2
    return [x if i % 2 == 0 else x + 1 for i, x in enumerate(range(n, 0, -2), 1)]

