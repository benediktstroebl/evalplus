
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
    # My coding solution:
    # res = [n]
    # while n != 1:
    #     if n % 2 == 0:
    #         n = n // 2
    #     else:
    #         n = n + 1
    #     res.append(n)
    # return res

    # A nicer solution proposed by one of the forum members:
    if n % 2 == 0:
        return [n] + make_a_pile(n // 2)
    return [n] + make_a_pile(n + 1)

