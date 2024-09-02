
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
    # Base case: the pile is only one level, return the number of stones in it.
    if n == 1:
        return [n]
    # Recursive case
    else:
        # Get the number of stones in the previous level
        n_prev = make_a_pile(n-1)
        # Check if the previous level was even
        if n_prev[-1] % 2 == 0:
            # The next level has one more stone than the previous level
            n_next = n_prev[-1] + 1
        else:
            # The next level has two more stones than the previous level
            n_next = n_prev[-1] + 2
        # Append the number of stones in the next level to the previous level
        n_prev.append(n_next)
        # Return the number of stones in each level in a list
        return n_prev
