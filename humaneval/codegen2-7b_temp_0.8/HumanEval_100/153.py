
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
    numbers = [n]
    next_level = (n+1) if n % 2 == 0 else (n+2)
    while next_level <= (n+2)*n:
        numbers.append(next_level)
        next_level = next_level + (next_level + 1) if next_level % 2 == 0 else next_level + 2
    return numbers
