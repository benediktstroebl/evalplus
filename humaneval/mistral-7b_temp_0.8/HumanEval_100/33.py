
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
    # Initialize a list to store the number of stones in each level.
    pile = []

    # Create an odd number if n is odd, else create an even number.
    if n % 2 == 1:
        num = n + 1
    else:
        num = n + 2

    # Append the number of stones in the first level to the list.
    pile.append(n)

    # Iterate through the levels of the pile and append the number of stones
    # in each level to the list.
    for i in range(1, int(num / 2) + 1):
        if num % 2 == 1:
            pile.append(i * 2 + 1)
        else:
            pile.append(i * 2)

    # Return the list of stones in each level.
    return pile

