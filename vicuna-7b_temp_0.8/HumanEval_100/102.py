
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
    # if n is odd, the number of stones in the next level is the next odd number
    # if n is even, the number of stones in the next level is the next even number
    if n % 2 == 0:
        # if n is even, we need to add 2 to the number of stones in the next level
        next_level = n + 2
    else:
        # if n is odd, we need to add 2 to the number of stones in the next level
        next_level = n + 1
    # initialize the list of stones for the next level
    next_level_stones = [next_level]
    # for each level, the number of stones in the previous level is the number of stones in the current level
    level_stones = [n]
    # we want to count the number of stones in the current and next levels
    for current_level_stones in level_stones:
        # for each pile of stones in the current level
        for i in range(current_level_stones):
            # if the pile is not empty, we want to add the number of stones in the pile to the next level
            if current_level_stones - i > 0:
                next_level_stones[0] += current_level_stones - i
        # increment the number of stones in the current level
        level_stones.append(current_level_stones)
        # add the next level stones
        next_level_stones.append(next_level_stones[0])
    return level_stones
