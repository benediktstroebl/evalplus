
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
    a = [0 for x in range(0, n+1)]
    b = [1]
    if n % 2 != 0:
        b.append(3)
    else:
        b.append(2)

    for i in range(1, n+1):
        if i % 2 == 0:
            a[i] = b[i-1] + 2
            b.append(a[i])
        else:
            a[i] = b[i-1] + 1
            b.append(a[i])
    return a
