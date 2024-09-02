
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
        raise ValueError("Parameter n should be a positive integer!")

    pile = [n]
    next_num = n

    while True:
        if next_num % 2 == 1:
            next_num -= 1
        elif next_num % 2 == 0:
            next_num += 1
        else:
            raise ValueError("Something went wrong!")

        pile.append(next_num)
        if next_num <= 1:
            return pile

