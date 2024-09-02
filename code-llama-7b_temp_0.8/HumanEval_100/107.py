
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
    # Create an empty list to hold the number of stones in each level.
    pile = []

    # Add the first level of stones to the list.
    pile.append(n)

    # Loop until the number of stones is 0.
    while n > 0:
        # If n is odd, add the next odd number of stones.
        if n % 2 != 0:
            n += 1

        # If n is even, add the next even number of stones.
        else:
            n += 2

        # Add the number of stones in the current level to the list.
        pile.append(n)

    # Return the list of stones in each level.
    return pile

