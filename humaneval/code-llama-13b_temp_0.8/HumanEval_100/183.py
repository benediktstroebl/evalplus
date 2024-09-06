
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
    result = []
    odd_pile = True
    stones = n
    while stones > 0:
        result.append(stones)
        stones = stones - 1 if odd_pile else stones + 1
        odd_pile = not odd_pile

    return result

