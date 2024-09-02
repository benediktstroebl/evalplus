
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
    # You can make a pile like this
    # [3, 5, 7]
    # [3, 4, 5, 6, 7]
    # [3, 2, 3, 4, 5, 6, 7]
    # Notice how the next level is always one less than the sum of the previous level
    pile = []
    level = 0
    while n > 0:
        level += 1
        pile.append(n)
        if n % 2 == 0:  # n is even
            n -= 1
        else:  # n is odd
            n -= 2
    return pile[::-1]

