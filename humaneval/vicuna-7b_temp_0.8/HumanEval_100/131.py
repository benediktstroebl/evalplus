
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
    # compute the next odd number
    if n % 2 == 1:
        next_odd = 2 * n + 1
    else:
        next_odd = n + 2

    # initialize the list of levels
    levels = [n]

    # compute the number of stones in each level
    for i in range(2, int(np.ceil(np.sqrt(n))) - 1):
        levels.append(n // i)

    # add the last level with the next odd number of stones
    levels.append(next_odd // 2)

    return levels