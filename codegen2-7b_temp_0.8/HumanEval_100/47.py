
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
    if n < 0:
        return "Input is not positive"
    elif n == 0:
        return [n]
    else:
        list_of_stones = [n]
        current_level = 2
        next_level = current_level + 1
        while next_level < n:
            current_level = next_level
            next_level = next_level + 1
            list_of_stones.append(current_level)
        return list_of
