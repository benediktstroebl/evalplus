
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
    # Store the number of stones in each level
    level_count = [n]

    # If n is odd, add 2, if even add 4
    for i in range(2, n+1):
        level_count.append(i+2 if n % i == 0 else i+4)

    # Sort the levels in ascending order
    level_count.sort(reverse=True)

    return level_count
