
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

    nums = [0, 1, 1, 3, 5]
    level = 1
    num_stones = 3
    while level < n:
        num_stones += 2
        level += 1
        nums.append(num_stones)
    return nums[1 : n + 1]
