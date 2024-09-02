
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
    # solving the problem
    # NOTE: This solution is quite inefficient as it uses a lot of recursive calls.
    # A more efficient solution can be found by using a sliding window approach
    # and using an iterative approach instead of a recursive one.

    def helper(n):
        if n == 0:
            return [0]
        if n == 1:
            return [1]

        result = []
        if n % 2 == 1:
            result.append(n)
            for i in range(2, n + 1):
                result.append(i)
        else:
            result.append(n)
            for i in range(2, n + 1):
                result.append(i)
        helper(n - 1)
        return result

    return helper(n)
