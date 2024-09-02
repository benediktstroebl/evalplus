
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
    # base case
    if n == 0:
        return []
    # compute the number of stones in the next odd level
    if n % 2 == 1:
        level_num = n + 1
        while n % 2 == 1:
            level_num += 2
            n = n // 2
        level_stones = [n]
    # compute the number of stones in the next even level
    elif n % 2 == 0:
        level_num = n + 1
        while n % 2 == 0:
            level_num += 2
            n = n // 2
        level_stones = [n]
    # add the current level stones to the next level
    level_stones.extend(range(1, level_num + 1))
    return level_stones