
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
    stone_piles = []
    stone_piles.append(n)
    while len(stone_piles) < 2:
        next_stone = (stone_piles[-1] - 1) // 2
        if next_stone > 0:
            stone_piles.append(next_stone)
        else:
            stone_piles.append(1)
    return stone_piles

