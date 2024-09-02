
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
    # Start the pile at level 1.
    pile = [n]
    # While there are still levels to make.
    while len(pile) > 0:
        # Get the number of stones in the last level.
        stones_in_last_level = pile[-1]
        # If that number is odd, add one level of stones.
        if stones_in_last_level % 2 == 1:
            pile.append(stones_in_last_level + 2)
        # Otherwise, add two levels of stones.
        else:
            pile.append(stones_in_last_level + 2)
            pile.append(stones_in_last_level + 2)
        #print(pile)
    return pile

