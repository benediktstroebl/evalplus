
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
    # The list to store the number of stones in each level
    stones = [0] * n + [1]

    # The number of levels is the number of stones
    levels = [n]

    # For each odd number i from 1 to n-1
    for i in range(1, n-1):
        # The number of stones in the next level is the next odd number if n is odd,
        # or the next even number if n is even
        if n % 2 == 0:
            # We take the next even number
            stones[i+1] = 2 * stones[i]
            # We add 1 to the number of stones in the next level
            levels[i+1] = levels[i] + 1
        else:
            # We take the next odd number
            stones[i+1] = 2 * stones[i] + 1
            # We add 1 to the number of stones in the next level
            levels[i+1] = levels[i] + 1

    # Return the list of stones in each level
    return levels[1:]
