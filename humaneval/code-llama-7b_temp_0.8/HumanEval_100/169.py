
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
    # your code here

    # made the nth level first
    nth_level = n

    # initialize the pile
    pile = []

    # add the nth level first
    pile.append(nth_level)

    # loop until pile is full
    while len(pile) < n + 1:
        # odd n
        if nth_level % 2 == 1:
            # add the next odd number
            pile.append(nth_level + 2)
        # even n
        elif nth_level % 2 == 0:
            # add the next even number
            pile.append(nth_level + 2)
        # update the nth_level
        nth_level += 2

    # return the pile
    return pile

