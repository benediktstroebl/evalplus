
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
        odd_n = n + 2
    else:
        odd_n = n + 1
    levels = [n]
    for i in range(2, odd_n + 1):
        levels.append(i)
        for j in range(1, i + 1):
            levels[i] += levels[i - 1]
    return levels
