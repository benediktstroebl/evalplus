
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
    total_stone = [n]
    if n % 2 == 0:
        num_stone = n
    else:
        num_stone = n - 1
    if n % 2 == 0:
        next_level = n + 1
    else:
        next_level = n + 2
    while next_level > num_stone:
        num_stone += (next_level - num_stone - 1)
        total_stone.append(num_stone)
        next_level += 2
    return total_stone
