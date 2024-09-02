
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
    # Create a list of the odd numbers up to the square root of n
    if n > 1:
        if n % 2 == 0:
            odd_numbers = range(3, int(n ** 0.5) + 1)
        else:
            odd_numbers = range(3, n + 1, 2)
    else:
        odd_numbers = range(3)

    # Create a list of the even numbers up to the square root of n
    even_numbers = [x for x in range(2, int(n ** 0.5) + 1) if n % x == 0]

    # Initialize the list of piles
    piles = [list(odd_numbers)]

    # Add a pile for each odd number
    for i in odd_numbers:
        piles.append([0] * (i - 1) + [1])

    # Add a pile for the last number
    piles.append([0] * (n - 1) + [1])

    # Create a list of the number of stones in each pile
    return [len(pile) for pile in piles]
