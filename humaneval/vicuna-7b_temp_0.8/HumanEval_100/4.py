
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
    # Create the pile of n levels of stones
    pile = []
    for i in range(n):
        pile.append(n)

    # Determine the number of stones in each level
    level_count = [0] * n + [1] * (n - 1)
    stones = [0] * n
    next_odd = [0] * n
    next_even = [0] * n
    for i in range(2, n + 1):
        if n % i == 0:
            level_count[n // i] = i ** 2
        else:
            level_count[n // i] = i + 1

        next_odd[n // i] = i + 1
        next_even[n // i] = i + 1
        stones[n // i] = i

    # Return the number of stones in each level
    return level_count, stones, next_odd, next_even
