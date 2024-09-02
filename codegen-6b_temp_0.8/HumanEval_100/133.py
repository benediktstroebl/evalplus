
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
    level = [n]

    if n % 2 == 0:
        temp = n // 2
    else:
        temp = (n + 1) // 2

    for i in range(1, temp):
        level.append(level[i - 1] + 2 * i)

    while temp > 0:
        level.append(level[temp - 1] + 1)
        temp -= 1

    return level
