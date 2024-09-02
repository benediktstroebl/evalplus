
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
    stones = [n]
    # starting from second level
    for i in range(1, n + 1):
        if n % i == 0:
            # if n is divisible by i, it means it's an even number, so
            # the next odd number is i+2
            next_odd = i + 2
        else:
            # if n is not divisible by i, it means it's an odd number, so
            # the next even number is i+1
            next_even = i + 1
        stones.append(next_odd)
        stones.append(next_even)
    return stones
