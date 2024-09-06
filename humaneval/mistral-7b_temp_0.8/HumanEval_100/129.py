
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
    # First level has n stones
    level1 = n
    # Number of stones in next level is either the next odd number or the next
    # even number
    next_odd_num = level1 + 2
    next_even_num = level1 + 4
    if level1 % 2 == 1:
        # level1 is odd, so use next odd number
        level2 = next_odd_num
    else:
        # level1 is even, so use next even number
        level2 = next_even_num
    # Keep going until we reach the number of levels
    result = [level1]
    for i in range(1, n):
        if level2 % 2 == 1:
            # level2 is odd, so use next odd number
            level2 = level2 + 2
        else:
            # level2 is even, so use next even number
            level2 = level2 + 4
        result.append(level2)
    return result

