
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

    assert n > 0, "n must be a positive integer"
    lst = []
    for i in range(n):
        if i == 0:
            lst.append(n)
        elif n % 2 == 0:
            lst.append(n + 1)
        elif n % 2 == 1:
            lst.append(n + 2)
        n -= 1
    return lst
