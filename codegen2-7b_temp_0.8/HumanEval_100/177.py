
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
    if not isinstance(n, int):
        raise TypeError("n is not an integer")
    if n < 0:
        raise ValueError("n is not greater than or equal to 0")

    return [n] + sum(
        [make_a_pile(next_odd_even(n)) for _ in range(1, n + 1)], []
    )

