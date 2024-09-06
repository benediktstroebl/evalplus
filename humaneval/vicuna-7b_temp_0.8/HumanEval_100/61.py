
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
    stack = []
    d = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4, 11: 4, 12: 4, 13: 5, 14: 5, 15: 5, 16: 6, 17: 6, 18: 6, 19: 6, 20: 7, 21: 7, 22: 7, 23: 7, 24: 8, 25: 8, 26: 8, 27: 8, 28: 8, 29: 9, 30: 9, 31: 9, 32: 9, 33: 10, 34: 10, 35: 10, 36: 10, 37: 11, 38: 11, 39: 11, 40: 11}

    for i in range(n):
        if n % 2 == 0:
            while stack:
                d.pop(stack.pop(0))
        else:
            while stack:
                d.pop(stack.pop(0))
        stack.append(d[i])
    return stack
