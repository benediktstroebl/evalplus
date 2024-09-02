
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
    # if n is odd, we have to check the next odd number
    if n % 2 == 1:
        result = [n]
        for i in range(2, n+1):
            result.append(i)
            result.append(i-1)
    # if n is even, we have to check the next even number
    elif n % 2 == 0:
        result = [n]
        for i in range(2, n+1):
            result.append(i)
            result.append(i)
    # if n is odd and odd number is taken, we have to adjust number of stones
    elif n % 2 == 1 and n % (n//2+1) == 0:
        result = [n]
        for i in range(2, n+1):
            result.append(i)
        result.append(result[-1]-1)
    # if n is even and even number is taken, we have to adjust number of stones
    elif n % 2 == 0 and n % (n//2+1) == 0:
        result = [n]
        for i in range(2, n+1):
            result.append(i)
        result.append(result[-1])
    return result
