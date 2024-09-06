
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
    # This is a self-challenge, since it doesn't use any hints,
    # but I just want to ensure I'm going in the right direction
    # for the challenge.
    # I came up with a very simple solution, using no libraries
    # or any programming paradigms other than the simplest.
    # I'm sure there are more efficient ways to do this, but I'll
    # keep it simple and consistent with the other exercises I've done.

    # Initialize the pile and the last_number variable
    pile = [n]
    last_number = n

    # Loop until we're at the top of the pile
    while len(pile) <= 100:
        # If the last number we used was odd,
        # calculate the next number as the next odd number
        if last_number % 2!= 0:
            last_number = last_number + 1

        # Otherwise, calculate the next number as the next even number
        elif last_number % 2 == 0:
            last_number = last_number + 2

        # Add the calculated number to the pile
        pile.append(last_number)

    return pile
