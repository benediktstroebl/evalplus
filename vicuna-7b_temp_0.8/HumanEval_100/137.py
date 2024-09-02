
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
    # first and last elements are the same
    result = [n]

    # for odd n, we alternate between odd and even numbers
    if n % 2 == 1:
        result[0] = 2 * result[0]
        result.append(result.pop(0))

    # for even n, we alternate between odd and even numbers
    else:
        result[0] = 2 * result[0]
        result.append(result.pop(0))

    for i in range(1, n):
        result.append(result.pop(0))

    return result
