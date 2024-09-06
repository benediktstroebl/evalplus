
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
    levels = [n]
    current_level = [n]
    while current_level[-1] < n//2:
        next_odd = True
        for i in range(2, n+1):
            if i % 2 == 0:
                next_odd = False
                break
        next_even = True
        for i in range(2, n+1):
            if i % 2 == 0:
                next_even = False
                break
        current_level.append(min(next_odd, next_even))
        levels.append(current_level[-1])
        current_level = [x for x in current_level if x != current_level[-1]]
    return levels