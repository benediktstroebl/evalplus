
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
    # ---------- the simplest way to solve it ----------
    num_stones = n
    result = []
    while num_stones > 0:
        result.append(num_stones)
        if num_stones % 2 == 1:  # odd number
            num_stones = num_stones * 3 + 1
        else:  # even number
            num_stones = num_stones // 2
    return result

    # ---------- a bit different solution using list comprehension ----------
    num_stones = n
    result = []
    while num_stones > 0:
        result.append(num_stones)
        if num_stones % 2 == 1:  # odd number
            num_stones = 3 * num_stones + 1
        else:  # even number
            num_stones = num_stones // 2
    return [result[i] for i in range(len(result) - 1, -1, -1)]

    # ---------- a bit different solution using tail recursion ----------
    def tail_recursion(num_stones, result):
        if num_stones > 0:
            return tail_recursion(
                num_stones,
                [num_stones] + result)
        return result

    return tail_recursion(n, [])

