
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
    # The number of possible next odd numbers from 3 to n.
    odd_numbers = [i for i in range(4, n + 1) if i % 2 == 1]

    # The number of possible next even numbers from 4 to n.
    even_numbers = [i for i in range(5, n + 1) if i % 2 == 0]

    # The number of possible next odd numbers from 3 to n.
    odd_numbers = [i for i in range(4, n + 1) if i % 2 == 1]

    # The number of possible next even numbers from 4 to n.
    even_numbers = [i for i in range(5, n + 1) if i % 2 == 0]

    return odd_numbers + even_numbers
