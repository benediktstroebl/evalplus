
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
    levels = [n]
    while len(levels) > 0:
        odd_or_even = -1
        if n % 2 == 0:
            odd_or_even = 0
        else:
            odd_or_even = 1

        level_size = odd_or_even * (n // 2)
        levels.append(level_size)
        n = n // 2

        if n > 0:
            odd_or_even = -1

    return levels
