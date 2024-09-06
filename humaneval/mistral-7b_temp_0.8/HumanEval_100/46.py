
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

    if n % 2 == 1:
        #if odd
        odd_stack = []
        for i in range(1, n + 1):
            odd_stack.append((i - 1)*2 + 1)
        return odd_stack
    else:
        #if even
        even_stack = []
        for i in range(1, n + 1):
            even_stack.append(i*2)
        return even_stack
