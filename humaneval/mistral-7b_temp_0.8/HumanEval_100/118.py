
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
    levels = []
    num = n
    i = 0
    while num > 0:
        levels.append(num)
        if i % 2 == 0:
            num = num + 2
        else:
            num = num + 1
        i += 1
    return levels
