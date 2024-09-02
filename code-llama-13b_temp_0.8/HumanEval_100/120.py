
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
    # ======================= UNSOLVED =======================

    result = []
    n_odd = True if n % 2 else False
    if n_odd:
        # when n is odd, then the next odd number is n + 1
        result = [n + 1]
    else:
        # when n is even, then the next even number is n + 2
        result = [n + 2]
    return result

