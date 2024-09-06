
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
    # Finding the next odd or even number
    if n % 2 == 0:
        next_num = n + 1
    else:
        next_num = 2 * n + 1

    # Making the pile
    pile = [n]
    while next_num > 1:
        for i in range(1, next_num):
            pile.append(pile[-1] + i)
        next_num -= 2

    return pile
