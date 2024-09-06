
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
    # Step 1: define a helper function
    def helper(n):
        if n % 2 == 0:
            return n+1
        else:
            return n+2
    
    # Step 2: initialize the result list
    result = []
    # Step 3: base case
    if n <= 0:
        return result
    # Step 4: use recursion
    result.append(n)
    return result + make_a_pile(helper(n))
