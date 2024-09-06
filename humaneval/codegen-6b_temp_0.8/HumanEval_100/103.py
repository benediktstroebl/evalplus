
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
    if n == 1:
        return [1]

    i = 0
    current_stones = 1
    current_level = [1]
    while i < n - 1:
        current_stones = current_level[i] + 2
        current_level.append(current_stones)
        i += 1
    return current_level

