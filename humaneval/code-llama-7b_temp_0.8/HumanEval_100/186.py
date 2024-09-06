
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
    if n < 1:
        raise ValueError("n must be a positive integer")
    result = [n]
    i = 0
    while i < n - 1:
        next_level_stones = result[i] + 2 if result[i] % 2 == 0 else result[i] + 1
        result.append(next_level_stones)
        i += 1
    return result
