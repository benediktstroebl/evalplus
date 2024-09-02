
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
    return [n] + [
        sum(
            [
                n // 2 * (i + 1) ** 2
                for i in range(int(n / 2))
            ]
        )
        for n in range(1, int(n ** 0.5) + 1)
    ]

