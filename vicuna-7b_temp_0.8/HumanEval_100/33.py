
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
    stack = []
    n = max(n, 1)
    for i in range(n):
        if n % 2 == 0:
            stack.append(n)
        else:
            stack.append(n-1)
    result = []
    for i in stack:
        for j in range(i):
            result.append(i)
    return result
