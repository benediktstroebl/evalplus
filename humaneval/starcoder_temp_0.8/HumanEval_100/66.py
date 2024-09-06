
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
    # # Make a list to store the answer.
    # answer = []
    # # Initialize current level to 1.
    # current_level = 1
    # while current_level <= n:
    #     # Append the number of stones in current level to the list.
    #     answer.append(current_level)
    #     # If current level is odd, add one to the current level.
    #     if current_level % 2 == 1:
    #         current_level += 1
    #     # If current level is even, subtract one to the current level.
    #     else:
    #         current_level -= 1
    # # Return the answer.
    # return answer
    # ------------------------------
    # Simplified version by using the append() method in a for loop:
    # Initialize answer to an empty list.
    answer = []
    # Append the first level to the list.
    answer.append(1)
    # For loop with range starting at level 2 to level n + 1:
    for i in range(2, n + 1):
        # If the current level is odd, add one to the current level.
        if i % 2 == 1:
            answer.append(i + 1)
        # If the current level is even, subtract one to the current level.
        else:
            answer.append(i - 1)
    # Return the answer.
    return answer
