
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
    # Hint 1: Simulate the process.
    # Hint 2: Once the number of stones in the next level is odd or even, it
    # remains like that.

    # Solution 1: Recursion
    #   - Recursive solution.
    #   - O(n) time complexity.
    #   - O(n) space complexity.
    # Solution 2: Iterative
    #   - Iterative solution.
    #   - O(n) time complexity.
    #   - O(1) space complexity.
    # Note:
    #   - Since the problem gives us a positive integer n, we can conclude that
    #     the number of levels is between 1 and n.
    #   - The result is an iterable object.

    # For a given n, the number of levels is always n.
    pile = [0] * n

    # A valid pile should always have a level 1 with n stones.
    pile[0] = n

    # A pile has at least 1 level.
    level = 1
    while level < n:
        # The number of stones in the next level is either the next odd or the
        # next even.
        stones = pile[level - 1] - 1
        if stones % 2 != 0:
            stones = stones - 1
        else:
            stones = stones + 1
        pile[level] = stones
        level = level + 1

    return pile

