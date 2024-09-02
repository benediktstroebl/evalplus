
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
    # initialize a list to store the number of stones in each level
    levels = [n]

    if n % 2 == 0:
        # if n is even, we need to add the next even number to the list
        levels.append(n + 2)
    else:
        # if n is odd, we need to add the next odd number to the list
        levels.append(n + 1)

    for i in range(1, n + 1):
        # for each level except the last one
        # we add the number of stones in the next level, which is either
        # the next odd number or the next even number
        # depending on the parity of n
        levels.append(levels[i - 1] + (n % 2 + 1))

    return levels