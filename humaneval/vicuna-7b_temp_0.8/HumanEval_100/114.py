
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
    # Count the number of odd and even numbers less than n
    odd = 0
    even = 0
    for i in range(1, n+1):
        if n % i == 0:
            even += i
        else:
            odd += i

    # Initialize list to store the number of stones in each level
    levels = [n]

    # Count the number of odd and even numbers greater than n
    while odd > 0:
        # If the current odd number is greater than n, subtract it from n
        n = n - odd
        odd = 0

        # Add the current odd number to the list
        levels.append(odd)

    # Count the number of odd and even numbers greater than n
    while even > 0:
        # If the current even number is greater than n, subtract it from n
        n = n - even
        even = 0

        # Add the current even number to the list
        levels.append(even)

    return levels
