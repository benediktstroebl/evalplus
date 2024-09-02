
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
    result = []

    for i in range(1, n+1):
        # print(f"i = {i}")
        # print(f"i % 2 = {i % 2}")
        # print(f"i / 2 = {i / 2}")
        # print(f"i / 2 - 2 = {i / 2 - 2}")
        # print(f"i / 2 if i % 2 == 0 else i / 2 - 1 = {i / 2 if i % 2 == 0 else i / 2 - 1}")

        if i % 2 == 0:
            result.append(i / 2 if i % 2 == 0 else i / 2 - 1)
        else:
            result.append(i + 1)

        # print(result)

    return result

