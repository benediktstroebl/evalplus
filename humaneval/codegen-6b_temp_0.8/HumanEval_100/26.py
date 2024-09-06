
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
    level_list = []
    # n = 0
    if n == 0:
        level_list = [0]
    else:
        if n % 2 == 0:
            level_list.append(n)
            level_list.append(n+2)
            n = n + 3
        else:
            level_list.append(n)
            level_list.append(n + 2)
            n = n + 3

        while n != 0:
            if n % 2 == 0:
                level_list.append(n)
                n = n + 2
            else:
                level_list.append(n)
                n = n + 2
    return level_list

