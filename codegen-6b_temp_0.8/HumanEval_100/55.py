
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
    stones = []
    for i in range(n):
        stones.append((i + 1) * (i % 2))
    stone = stones[:]
    for j in range(len(stones) - 1, -1, -1):
        stone[j] = stone[j] - 1
        stones[j] = stone[j]

    return stones

