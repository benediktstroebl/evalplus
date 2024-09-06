
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
    n = int(n)
    levels = []
    if n%2 == 1:
        for i in range(1,n):
            if i == 0:
                level = n
            elif i%2 == 1:
                level += 2
            else:
                level += 4
            levels.append(level)
        return levels
    if n%2 == 0:
        for i in range(1,n):
            if i == 0:
                level = n
            elif i%2 == 1:
                level += 2
            else:
                level += 4
            levels.append(level)
        return levels

