
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
    # Initialize an empty list to store the number of stones in each level
    levels = []

    # If n is odd, add the next odd number to the levels list
    if n % 2 == 1:
        levels.append(n + 1)

    # If n is even, add the next even number to the levels list
    elif n % 2 == 0:
        levels.append(n + 2)

    # Add the remaining odd numbers to the levels list
    for i in range(3, n+1, 2):
        levels.append(i)

    return levels
