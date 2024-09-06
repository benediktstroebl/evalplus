
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
    # initialize an empty list to store the number of stones in each level
    levels = []
    # if n is odd, the number of stones in the first level will be n
    if n % 2 == 1:
        levels.append(n)
    # for each subsequent level, add the number of stones in the previous level
    for i in range(2, n + 1):
        levels.append(levels[i-2] + (i % 2 == 1 and 1 or -1))
    return levels
