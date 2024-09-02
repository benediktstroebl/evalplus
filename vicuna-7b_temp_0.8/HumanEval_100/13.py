
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
    # 1 is the number of stones in the first level
    levels = [1]

    # 2 is the number of stones in the second level
    if n % 2 == 0:
        levels.append(n)
    else:
        levels.append(n-1)

    # 3 is the number of stones in the third level
    for i in range(2, n+1):
        levels.append(i)
        levels.append(i-1)

    return levels
