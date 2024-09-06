
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
    # A solution using recursion:
    # if n is odd, the next odd number is: n + 2
    # else, the next odd number is: n + 1
    # Therefore, the function recursive_pile will look like this:
    # def recursive_pile(n, step):
    #     if n == 0:
    #         return []
    #     return [n] + recursive_pile(n + step, step)
    # return recursive_pile(n, step=2 - (n % 2))

    # A solution using iteration:
    if n <= 0:
        return []
    if n == 1:
        return [1]
    pile = [n]
    next_level = n + 2 - (n % 2)
    while next_level > 1:
        pile.append(next_level)
        next_level = next_level + 2 - (next_level % 2)
    return pile
