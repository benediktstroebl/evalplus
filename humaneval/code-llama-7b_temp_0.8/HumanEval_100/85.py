
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

    """
    It's a great idea to make small tests to check if your function works as
    expected. So you can quickly find a mistake in your code.

    A good idea is to test a few different inputs.

    Here's one way to implement this function:
    """

    # pile = []
    # for i in range(n):
    #     pile.append(2 * i + 1)
    # return pile

    """
    You can also use list comprehensions. They're shorter and more concise.
    """
    # return [2 * i + 1 for i in range(n)]

    """
    Here's another approach using recursion:
    """
    if n == 0:
        return []

    return [2 * n + 1] + make_a_pile(n - 1)

