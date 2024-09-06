
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
    if n % 2 == 0:
        stones = [n]
        for i in range(1, n+1):
            stones.append(stones[i-1] + stones[i-2])
        return stones
    else:
        stones = [n-1, n-1, n-1]
        for i in range(2, n+1):
            if n % i == 0:
                stones[i-1] = n - i
            else:
                stones[i-1] = n - i - 1
        return stones
