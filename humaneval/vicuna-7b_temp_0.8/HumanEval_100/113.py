
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
    stones = [0] * n
    n_levels = [n]
    pile = [n_levels]
    for i in range(1, n + 1):
        if n % i == 0:
            even_number = i
        else:
            odd_number = i
            for j in range(n_levels[-1]):
                pile[-1].append(even_number)
            pile.append(list(range(even_number, odd_number + 1)))
            n_levels.append(even_number)
    for i in range(n_levels[-1]):
        pile[-1].append(n_levels[-2])
    return pile
