
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

    # Create a list of the number of stones in each level
    # First level is the number
    # Next level is the next odd number if n is odd
    # Next level is the next even number if n is even

    # If n is odd, then the next level should be the next odd number
    # If n is even, then the next level should be the next even number
    # To find the next odd number, we can use the formula: (2n+1)
    # To find the next even number, we can use the formula: 2n
    if n % 2 == 1:
        next_odd = (2 * n + 1)
    else:
        next_even = 2 * n

    return [n, next_odd, next_even]
