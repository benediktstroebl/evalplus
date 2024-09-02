
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
    # Recursive solution.
    # Time: O(n), Space: O(n)
    # if n < 1:
    #     return []

    # if n % 2 == 0:
    #     n += 1

    # return [n] + make_a_pile(n + 2)

    # Iterative solution.
    # Time: O(n), Space: O(1)
    result = []
    count = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 2
        else:
            count += 1
        result.append(count)

    return result

