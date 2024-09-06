
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
    "*** YOUR CODE HERE ***"
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n > 1:
        if n % 2 == 1:
            level = [n] + [n+2*(i+1) for i in range(n-1)]
        else:
            level = [n] + [n+2*(i) for i in range(n-1)]
        return level
