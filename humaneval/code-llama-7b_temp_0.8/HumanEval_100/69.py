
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
    # if n is odd:
    #     make a list with n, n+2, n+4
    # else:
    #     make a list with n, n+2
    # return the list

    # pseudocode:
    # if n is odd:
    #     make a list with n, n+2, n+4
    # else:
    #     make a list with n, n+2
    # return the list

    # 1. base cases
    # if n is smaller than 1, return empty list
    if n < 1:
        return []
    # if n is 1, return [1]
    if n == 1:
        return [1]

    # 2. recursivity
    # add the first element of the recursive call
    # add the other elements in a loop
    # return the list

    # pseudocode:
    # if n is odd:
    #     make a list with n, n+2, n+4
    # else:
    #     make a list with n, n+2
    # return the list

    # 1. base cases
    # if n is smaller than 1, return empty list
    if n < 1:
        return []
    # if n is 1, return [1]
    if n == 1:
        return [1]

    # 2. recursivity
    # add the first element of the recursive call
    # add the other elements in a loop
    # return the list

    # pseudocode:
    # if n is odd:
    #     make a list with n, n+2, n+4
    # else:
    #     make a list with n, n+2
    # return the list
    return [n] + make_a_pile(n+2)

