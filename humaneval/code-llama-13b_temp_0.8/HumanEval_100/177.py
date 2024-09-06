
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
    # if n is odd then the next odd level is 1 more than the even level.
    # if n is even then the next even level is 1 more than the odd level.
    # let's use the modulo operator (%) to find out if n is odd or even
    # If n is even, % 2 is zero.
    # If n is odd, % 2 is 1.
    if n % 2 == 0:
        return [i for i in range(n, 0, -2)]
    else:
        return [i for i in range(n, 0, -1)]
