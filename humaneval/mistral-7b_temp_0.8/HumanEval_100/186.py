
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
    # 1st level has n stones
    # 2nd level has n+1 stones if n is odd
    # 2nd level has n+2 stones if n is even
    # 3rd level has n+3 stones if n is odd
    # 3rd level has n+4 stones if n is even
    # ...
    # n-th level has n+(n-1) stones
    #
    # example:
    # n = 3
    # n+1 = 4
    # n+2 = 5
    # n+3 = 6
    # n+4 = 7
    # n+5 = 8
    # n+6 = 9
    # n+7 = 10
    # n+8 = 11
    #
    # return [3, 5, 7, 9, 11]

    # n = 3
    # n+2 = 5
    # n+4 = 7
    # n+6 = 9
    # n+8 = 11
    # n+10
