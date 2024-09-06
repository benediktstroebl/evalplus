def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Define the list of digits from 0 to N-1, where N is the base representing the n-th power of 10
    base = 10 ** (n - 1)
    # Generate the permutations of digits from 0 to base-1 without repeating
    perms = [str(i) for i in range(base)] + [str(i) for i in range(base - 1, 0, -1)]
    # Count the permutations that start or end with 1
    return 2 * len(perms) // 2  # Divide by 2 to avoid double-counting, and multiply by 2 to account for both starting and ending 1s