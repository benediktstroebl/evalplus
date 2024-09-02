
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
    n_levels = 0
    n_stones = n
    results = []
    while n_stones != 1:
        n_stones = n_stones + 1 if n_stones % 2 else n_stones - 1
        n_levels += 1
        results.append(n_stones)
    results.append(1)
    return results
