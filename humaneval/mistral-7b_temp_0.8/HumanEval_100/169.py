
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
    # your code here
    if n == 0:
        return [0]
    else:
        odd = True
        if n % 2 == 0:
            odd = False
        levels = []
        for i in range(0, n):
            levels.append(i + 2)
        for i in range(0, len(levels)):
            if odd:
                levels[i] += 2
            else:
                levels[i] += 1
        return levels

