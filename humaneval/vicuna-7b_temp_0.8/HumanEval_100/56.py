
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
    # The number of stones on the first level
    stones = n
    # The number of stones on the next level
    next_level_stones = 0
    # The number of stones in the current level
    current_level_stones = 1
    # The number of odd numbers in n
    odd_count = 0
    # The number of even numbers in n
    even_count = 0

    if n % 2 == 0:
        odd_count = 0
        even_count = 1
    else:
        odd_count = 1
        even_count = 0

    # Repeat the process for each level
    while current_level_stones <= n:
        # Calculate the number of stones in the next level
        if n % 2 == 0:
            next_level_stones = odd_count
        else:
            next_level_stones = even_count
        # Update the number of stones in the current level
        current_level_stones += next_level_stones
        # Increment the number of odd numbers and even numbers in n
        odd_count += 1
        even_count += next_level_stones - odd_count

    return [stones, next_level_stones] + [current_level_stones] * (n // 2)