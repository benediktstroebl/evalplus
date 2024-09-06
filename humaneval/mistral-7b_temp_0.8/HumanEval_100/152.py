
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
    n = int(n)
    odd_pile = [3] + [5 * i for i in range(1, int(n/2))]
    even_pile = [4] + [6 * i for i in range(1, int(n/2))]
    if n % 2:
        return odd_pile
    return even_pile

