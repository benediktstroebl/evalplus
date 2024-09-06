
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
    # make a list to hold the results
    result = [n]

    # start with the number of stones
    stones = n

    # while we still have stones to pile, keep piling
    while stones:

        # if number of stones is odd, make next level with odd number of stones
        if stones % 2:
            stones = (stones * 3) + 1

        # if number of stones is even, make next level with even number of stones
        else:
            stones = stones * 2

        # add number of stones to result list
        result.append(stones)

    # return the result list
    return result
