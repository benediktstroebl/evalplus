
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
    # 0 represents the base of the pile, which is 1 less than the given n
    # n levels, 0 level has 0 stones
    base = 1
    result = [0] * (n+1)
    for i in range(n):
        result[i] = base
        base *= 2
    result += [base]
    for i in range(n-1, -1, -1):
        if n % i:
            result[i] += (i+1)
        else:
            result[i] += (i+2)
    return result