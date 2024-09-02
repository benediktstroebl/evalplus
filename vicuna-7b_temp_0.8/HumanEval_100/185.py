
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
    # initialize the list with the first level
    result = [n]
    if n % 2 == 0:
        next_level = [n]
    else:
        next_level = [2 * n + 1]
    # fill the list with the number of stones in each level
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(next_level[i - 1] - 1)
        else:
            result.append(next_level[i - 1])
    return result
