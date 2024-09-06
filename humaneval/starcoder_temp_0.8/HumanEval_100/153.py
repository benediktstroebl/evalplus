
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
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [2]

    even = n % 2 == 0
    if even:
        last_num = n + 1
    else:
        last_num = n

    prev_pile = make_a_pile(last_num)
    new_pile = [1] * len(prev_pile)
    for i, stone in enumerate(prev_pile):
        if i == 0:
            continue
        else:
            if even:
                new_pile[i] = prev_pile[i] + 1
            else:
                new_pile[i] = prev_pile[i] - 1

    return new_pile
