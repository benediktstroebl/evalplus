
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
    if n < 1:
        return []
    num_stones = n
    result = []
    while num_stones > 0:
        result.append(num_stones)
        if num_stones % 2 == 1:
            num_stones = num_stones * 3 + 1
        else:
            num_stones = num_stones * 3
        num_stones /= 2
    return result
