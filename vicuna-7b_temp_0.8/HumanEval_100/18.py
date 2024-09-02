
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
    # base case
    if n == 0:
        return []
    
    # recurrence relation
    # use 2 lists to keep track of the current number of stones
    # and the next odd number for odd n and the next even number
    # for even n
    even_next_number = [2]
    odd_next_number = [3]
    # initialize the result list
    result = [n]
    # iterate over the levels
    for i in range(n-1, -1, -1):
        # get the current number of stones
        current_number = result[i]
        # get the next odd number or next even number
        next_number = odd_next_number[i % 2] if i % 2 else even_next_number[i % 2]
        # add the current number of stones and the next number
        result.append(current_number + next_number)
    # return the result
    return result
