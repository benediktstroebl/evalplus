
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
    # Check if n is odd or even
    if n % 2 == 0:
        # If n is even, n = 2*k, where k is the smallest positive integer
        k = 1
    else:
        # If n is odd, n = 2*k + 1, where k is the smallest positive integer
        k = 1
    # Initialize a list to store the number of stones in each level
    levels = [n]
    # Keep adding the next odd or even number to the list, depending on n
    while n > 0:
        # If n is odd, add the next odd number
        if n % 2 == 1:
            levels.append(n + 1)
        # If n is even, add the next even number
        else:
            levels.append(n)
        # Decrement n
        n = n // 2
    # Return the list
    return levels
