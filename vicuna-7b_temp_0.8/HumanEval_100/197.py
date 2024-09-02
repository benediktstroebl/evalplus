
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
    def dfs(n, lvl):
        if n == 0:
            yield from lvl
        for i in range(n+1):
            for j in range(i+1):
                if i % 2 == 1 and j % 2 == 1:
                    yield from dfs(i-1, lvl+[i])
                elif i % 2 == 0 and j % 2 == 0:
                    yield from dfs(i-1, lvl+[j])
                yield i

    return list(dfs(n, [n]))