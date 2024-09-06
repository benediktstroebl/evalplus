
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
        raise TypeError('n must be an integer')
    if n < 1:
        raise ValueError('n must be positive')

    if n == 1:
        return [n]
    result = [n]
    if n % 2:
        result.append(n + 1)
    else:
        result.append(n - 1)

    for i in range(1, n):
        result.append(result[i - 1] + i + 1)
    return
