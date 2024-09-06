
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
    # Check if n is odd or even
    if n % 2 == 0:
        # If n is even, use next even number
        even_numbers = [2 * i for i in range(2, n+1)]
    else:
        # If n is odd, use next odd number
        odd_numbers = [2 * i + 1 for i in range(2, n+1)]

    # Initialize the list with one stone
    levels = [n]

    # Add next level
    for level in odd_numbers:
        # Add each odd number in list to current level
        levels.append(level)
        levels.append(level)

    # Add next level
    for level in even_numbers:
        # Add each even number in list to current level
        levels.append(level)
        levels.append(level)

    return levels
