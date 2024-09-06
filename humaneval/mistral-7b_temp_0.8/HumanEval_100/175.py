
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

    # A list to return
    stones = []

    # We start with 1 stone, to get the next even/odd number we get
    # the modulus of n+1
    if n % 2 == 0:
        n_stones = 2
    else:
        n_stones = 1

    # We get the next number from n_stones by using the modulus again
    while n > n_stones:
        if n_stones % 2 == 0:
            n_stones += 1
        else:
            n_stones += 2

        # We add n_stones to the list
        stones.append(n_stones)

    return stones
