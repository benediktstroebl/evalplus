
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
    # construct a list of integers representing the number of stones on each level
    levels = [n]
    if n % 2 == 0:
        # if n is even, make the next odd number the number of stones on the next level
        for i in range(1, n+1):
            if i % 2 == 1:
                levels.append(i+1)
    else:
        # if n is odd, make the next even number the number of stones on the next level
        for i in range(1, n+1):
            if i % 2 == 0:
                levels.append(i+1)
            else:
                levels.append(i)
    return levels
