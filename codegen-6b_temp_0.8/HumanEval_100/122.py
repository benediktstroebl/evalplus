
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
    if n == 1:
        return [1]
    if n % 2 == 1:
        next = n + 1
    else:
        next = n
    stones = make_a_pile(next)
    if n % 2 == 0:
        next = n - 1
    else:
        next = n
    while next > n:
        stones.append(stones[(n - 1) % (len(stones) - 1)] + stones[(n - 1) % (len(stones) - 1)])
        next -= 1
    return stones

