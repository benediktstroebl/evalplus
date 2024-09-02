
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
    if n <= 1:
        return [n]

    # calculate the number of odd and even numbers less than or equal to n/2
    odds = [i for i in range(1, n // 2 + 1) if i % 2 == 1]
    evens = [i for i in range(1, n // 2 + 1) if i % 2 == 0]

    # add the next odd number if n is odd
    if n % 2 == 1:
        odds.append(n)

    # add the next even number if n is even
    if n % 2 == 0:
        evens.append(n)

    # add the number of stones in the odd levels to the even levels
    result = []
    for i in range(1, len(odds) + 1):
        result.append(odds[i-1] + evens[i-1])

    return result