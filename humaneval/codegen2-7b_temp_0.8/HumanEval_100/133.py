
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
    list_levels = []
    if n % 2 == 1:
        list_levels.append(n)
    else:
        odd_number = n + 1
        even_number = n + 2
        list_levels.append(odd_number)
        list_levels.append(even_number)
    return list_
