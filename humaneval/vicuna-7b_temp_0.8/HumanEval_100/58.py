
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
        return [0]
    # make a list of next odd numbers if n is odd
    if n % 2 == 1:
        return [n] + [next_odd_number(n - 1) for i in range(1, n + 1)]
    # make a list of next even numbers if n is even
    return [n] + [next_even_number(n - 1) for i in range(1, n + 1)]
