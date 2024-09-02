
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

    # recursively call the function until the parameter is 1, return 1 as the
    # level value
    if n == 1:
        return [1]

    # if n is odd, the next level value should be odd, so we make a new pile of
    # odd numbers
    if n % 2!= 0:
        n = odd_pile(n)

    # if n is even, the next level value should be even, so we make a new pile
    # of even numbers
    else:
        n = even_pile(n)

    return [n] + make_a_pile(n)

