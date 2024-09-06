
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
    # Begin a base case if n is 1.
    if n == 1:
        return [1]
    
    # Create a list for each level, starting from the first level.
    # Each level will be an even number.
    level = 2
    
    # Create an empty list for all levels.
    levels = []
    
    # While the level is less than or equal to the number of levels (n).
    while level <= n:
        # Append to the list the number of stones in that level.
        levels.append(level)
        # Increment the level to the next even number.
        level += 2
        
    # Return the list of levels.
    return levels
