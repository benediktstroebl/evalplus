
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
    # We don't need to compute the next odd or even number for n odd or even
    levels = [n]
    while n > 0:
        # Compute the next level number
        next_level = 2 * n + 1 if n % 2 == 0 else n + 1
        # Remove the first n - 1 elements from the list
        levels = levels[1:]
        # Remove the number from the list
        levels.remove(next_level)
        # Add the number of stones to the pile
        levels.insert(int(next_level/2), 1)
        # Update the number of stones in the current level
        levels[0] += 1
        # Remove the number from the list
        levels.remove(int(next_level/2))
        # Update the number of stones in the current level
        levels[0] -= 1
        # The number of stones in the current level
        levels.insert(int(n/2), -1 * (n//2 - levels[-1]))
        # Update the number of stones in the current level
        levels[0] += int(n/2 - levels[-1])
        # Update the number of stones in the current level
        levels.insert(int(n/2), -1 * (n//2 - levels[-1]))
        # Update the number of stones in the current level
        levels.insert(int(n/2), -1 * (n//2 - levels[-1]))
        # Update the number of stones in the current level
        levels.insert(int(n/2), -1 * (n//2 - levels[-1]))
        # Update the number of stones in the current level
        levels.insert(int(n/2), -1 * (n//2 - levels[-1]))
        # Update the number of stones in the current level
        levels.insert(int(n/2), -1 * (n//2 - levels[-1]))
        # Update the number of stones in the current level
        levels.insert(int(n/2), -1 * (n//2 - levels[-1]))
        # Update the number of stones in the current level
        levels.insert(int(n/2), -1 *
