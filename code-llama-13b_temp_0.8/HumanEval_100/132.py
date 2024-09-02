
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
    # Hint 1: you can use "odd/even" as boolean conditions.
    # Hint 2: you can use modulo operator (%) to check if a number is odd or even.
    # Hint 3: remember that you can use while loop without incrementing n.

    # Solution below:
    result = []
    while n:
        result.append(n)
        n = (n % 2) + n
    return result

