
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
    # Using a recursive function to solve the problem
    def recursive(n):
        # If n is odd, we will use the next odd number
        if n % 2 == 1:
            return [n, n]
        # If n is even, we will use the next even number
        else:
            return [n, n + 2]
    return recursive(n)
