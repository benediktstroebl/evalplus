
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
        # Even n
        level = [n]
        for i in range(1, n + 1):
            level.append(level[i - 1] + 1)
        return level
    else:
        # Odd n
        level = [n]
        for i in range(2, n + 1):
            if n % i == 1:
                level.append(level[i - 2] + 1)
            else:
                level.append(level[i - 2] + 2)
        return level
