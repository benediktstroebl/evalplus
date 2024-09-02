
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
    # Define a helper function to calculate the number of stones in the next level
    def helper(n):
        if n < 1:
            return [1]
        else:
            if n % 2 == 0:
                return [n, helper(n+2)]
            else:
                return [n+1, helper(n+3)]

    # Get the number of stones in the first level
    return helper(n)[0]
