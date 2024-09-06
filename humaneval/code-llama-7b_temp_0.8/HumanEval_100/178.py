
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

    # Returned an empty list if n is less than 1
    if n < 1:
        return []

    # Initialized a variable to store the result
    result = []

    # Initialized a variable to store the number of stones in the first level
    n_of_stones = n

    # While loop to iterate over the number of levels
    while n_of_stones > 0:

        # If the number is odd, add the next odd number
        if n_of_stones % 2 != 0:
            result.append(n_of_stones + 1)

        # If the number is even, add the next even number
        else:
            result.append(n_of_stones + 2)

        # Decrement the number of stones by 1 level
        n_of_stones -= 1

    # Return the number of stones in each level in a list, where element at index
    # i represents the number of stones in the level (i+1)
    return result
