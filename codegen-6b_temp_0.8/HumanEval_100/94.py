
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
    def make_a_pile_rec(left, right, level):
        if left == right:
            return [level + 1]
        if (left + right) % 2 == 1:
            return make_a_pile_rec(left, (left + right) // 2, level + 1) + \
                   make_a_pile_rec(left + (left + right) // 2 + 1, right, level + 1)
        else:
            return make_a_pile_rec(left, (left + right) // 2, level + 1) + \
                   make_a_pile_rec((left + right) // 2 + 1, right, level + 1)

    return make_a_pile_rec(1, n, 1)
