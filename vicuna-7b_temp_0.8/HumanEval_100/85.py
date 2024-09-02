
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
    count = [0] * (n + 1)
    stones = [0] * (n + 1)
    for i in range(n + 1):
        if i % 2 == 0:
            stones[i] = 0
        else:
            stones[i] = 1
    level = 1
    for i in range(2, n + 1):
        if i % 2 == 0:
            count[level] = stones[level - 1]
            level += 1
        else:
            count[level] = i + 1
            stones[level] = i + 1
            level += 1
    return count