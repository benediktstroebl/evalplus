
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
    if n % 2 == 0:
        # The number of stones in the next level is the next even number
        next_level_stones = [2 * x for x in range(n)]
    else:
        # The number of stones in the next level is the next odd number
        next_level_stones = [2 * x + 1 for x in range(n)]
    
    # Create a list to store the number of stones in each level
    level_stones = [[0] * n for _ in range(n)]

    # Fill the first level
    level_stones[0][0] = n

    # Fill the next levels
    for i in range(1, n + 1):
        for j in range(i):
            level_stones[i][j] = level_stones[i - 1][j]
        for k in range(i, n + 1):
            level_stones[i][k - 1] = level_stones[i - 1][k]

    return level_stones
