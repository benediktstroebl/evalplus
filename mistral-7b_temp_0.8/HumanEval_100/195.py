
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
    # Make an empty list to store the number of stones in each level.
    # Start with n, which is the number of stones in the first level.
    # Make a for loop to go through the remaining levels.
    # If the level number is odd, add 2 to the number of stones in the previous level.
    # If the level number is even, multiply the number of stones in the previous level by 2.
    # Append the number of stones in the current level to the list.
    # Return the list.

    stones_per_level = []
    stones_per_level.append(n)
    for level in range(1,len(stones_per_level)):
        if level % 2 == 1:
            #number of stones in the current level is odd
            next_level_of_stones = 2 + stones_per_level[level-1]
        else:
            #number of stones in the current level is even
            next_level_of_stones = 2 * stones_per_level[level-1]
        stones_per_level.append(next
