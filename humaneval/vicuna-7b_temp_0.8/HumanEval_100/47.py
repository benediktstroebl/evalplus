
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
    # List to store the number of stones in each level
    levels = [n]

    # Calculate the next odd number if n is odd or the next even number if n is even
    while True:
        # If n is odd
        if n % 2 != 0:
            # Take the next odd number
            next_odd_num = n + 2
            # Update n and levels
            n, levels = n + 2, [n, next_odd_num]
            # Update the number of stones in the current level
            levels[0] += 1
        # If n is even
        else:
            # Take the next even number
            next_even_num = n + 2
            # Update n and levels
            n, levels = n + 2, [n, next_even_num]
            # Update the number of stones in the current level
            levels[0] += 1

        # If the next number is the same as n, it's the end of the list
        if next_odd_num == n or next_even_num == n:
            break

    # Return the list of levels
    return levels
