
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
    # Use a list to store the number of stones in each level
    stones = [0] * n

    # Start with the first level
    for i in range(1, n+1):
        stones[i] = n

    if n % 2 == 0:
        # If n is even, make the next level the next even number
        next_even = 2*n
        for i in range(2, n+1, 2):
            if n % i == 0:
                # If the next number is divisible by i, adjust the next even number
                next_even = i*next_even
            stones[i+1] = next_even
    else:
        # If n is odd, make the next level the next odd number
        next_odd = 2*n+1
        for i in range(1, n+1, 2):
            if n % i == 0:
                # If the next number is divisible by i, adjust the next odd number
                next_odd = i*next_odd
            stones[i+1] = next_odd

    return stones
