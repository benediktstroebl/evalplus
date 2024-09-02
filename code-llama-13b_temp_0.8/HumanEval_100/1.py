
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
    # 1. check input
    if n < 1:
        return []
    # 2. initialize result
    result = []
    # 3. calculate number of stones in first level
    stones = n
    # 4. add stones to result
    result.append(stones)
    # 5. calculate number of stones in next level
    # 5a. if n is odd, then the next odd number is 3n + 1
    if n % 2 == 1:
        stones = 3 * n + 1
    # 5b. if n is even, then the next even number is 2n + 2
    else:
        stones = 2 * n + 2
    # 6. add stones to result
    result.append(stones)
    # 7. repeat until last level
    while stones < 10000:
        # 7a. calculate number of stones in next level
        # 7b. if stones is odd, then the next odd number is 3n + 1
        if stones % 2 == 1:
            stones = 3 * stones + 1
        # 7c. if stones is even, then the next even number is 2n + 2
        else:
            stones = 2 * stones + 2
        # 7d. add stones to result
        result.append(stones)
    # 8. return result
    return result

