
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

    # divide by two, then add 0.5 to the result
    # this will give us the number of times we should add 1
    # to n to make it even
    n += int((n - 1) / 2) + 1

    # start with the initial number of stones
    # and add the number of stones for each level
    return [n] + [n + i for i in range(1, n - 1, 2)]

