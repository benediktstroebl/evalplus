
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
    # base case
    if n == 0:
        return []

    # initialize list of levels
    levels = [n]

    # loop to fill levels
    for i in range(1, n+1):
        # calculate level
        level = i

        if n % 2 == 0:
            # even number
            level += (n // 2)

        # calculate next number
        next_num = 2 * (i // 2) + 1

        # add level
        levels.append(level)

        # add number of stones
        levels.append(next_num)

    return levels
