
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
    # using recursion
    # add 1 to the number of stones in the previous level
    # if the current number is odd, add 2 to the number of stones in the current level
    # if the current number is even, add 2 to the number of stones in the current level
    # also, add 1 to the current number of stones
    stones = [n + 1]
    while len(stones) < n:
        stones.append(stones[len(stones) - 1] + (n % 2 == 0 and 2 or 1))
        n //= 2
    return stones
