
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
    # This function uses dynamic programming, which is a technique to solve problems recursively by breaking them down into smaller subproblems.
    # Each subproblem is a smaller version of the problem that is already solved.
    # By storing the solutions to all subproblems, we can quickly find the solution to the original problem.

    # We'll use a list to store the solutions, where element i represents the number of stones in the (i+1)th level.
    # We'll initialize the list with the correct solutions, except for the first element, which is the recursive call.
    solutions = [n]

    # Now, we'll fill in the rest of the list using a loop.
    for i in range(1, len(solutions)):
        if n % 2 == 0:
            # If n is even, the next odd number is n+2.
            solutions[i] = n + 2
        else:
            # If n is odd, the next odd number is n+1.
            solutions[i] = n + 1

    return solutions
