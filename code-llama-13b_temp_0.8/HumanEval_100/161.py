
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

    lst = [n]

    if n % 2 == 0:
        x = n
    else:
        x = n + 1

    while x > 0:
        lst.insert(0, x)
        if x % 2 == 0:
            x = x - 1
        else:
            x = x - 2
    return lst
