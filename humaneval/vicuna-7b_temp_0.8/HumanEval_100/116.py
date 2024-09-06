
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
    # Create a list of next numbers
    next_numbers = [2 * i + 1 if i % 2 == 0 else 2 * i + 2 for i in range(1, n + 1)]

    # Create a list of zeros to represent the pile
    pile = [0] * (n + 1)

    # Fill the pile with next numbers
    for i in range(1, n + 1):
        pile[i] = next_numbers.pop(0)

    # Return the pile
    return pile
