
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
    # Calculate the number of odd numbers less than or equal to n/2
    odd_numbers = [i for i in range(n//2) if i % 2 == 1]

    # Calculate the number of even numbers greater than or equal to n/2
    even_numbers = [i for i in range((n//2)+1) if i % 2 == 0]

    # Return the list with the number of stones in each level
    return odd_numbers + [i+1 for i in even_numbers]
