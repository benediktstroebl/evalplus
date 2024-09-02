
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
    # for j in range(n+1, 0, -1):
    #     if n % j == 0:
    #         level = [0] * j
    #         for i in range(1, n//j):
    #             level[i] = n // j
    #         return level
    #     else:
    #         level = [0] * j
    #         for i in range(1, n//j+1):
    #             level[i-1] += n % j
    #         return level
    if n % 2 == 0:
        level = [0] * (n+1)
        for i in range(2, n+1):
            level[i-2] += n // 2
            level[i-1] += 1
        return level
    else:
        level = [0] * (n+1)
        for i in range(2, n+1):
            level[i-2] += n // 2
            level[i-1] += 1
            level[i] += 1
        return level
