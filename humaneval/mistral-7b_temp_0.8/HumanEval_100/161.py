
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
    # Base Case
    if n == 0:
        return []
    # Make an empty list
    pile = []
    # Add the n stones to the pile
    pile.append(n)
    # Loop while the level is not 1
    while n > 1:
        # Find the next even number
        even = n + 1
        # Find the next odd number
        odd = n + 2
        # Check if the number of stones should be even or odd
        if n % 2 == 0:
            # If it should be even, add the even number to the pile
            n = even
        else:
            # If it should be odd, add the odd number to the pile
            n = odd
        # Add the number of stones to the pile
        pile.append(n)
    return pile
