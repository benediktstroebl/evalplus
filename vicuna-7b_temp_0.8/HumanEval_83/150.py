
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # This is a recursive solution, so we can get the solution by
    # looking at the pattern of the solution.
    # The pattern is: [1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2], [4, 1], [4, 2], ...
    # This pattern is formed by the recurrence relation:
    # T(n) = T(n-1) + T(n-2) + T(n-3)
    # We can implement this recurrence relation using two for-loops
    # to compute the number of 1s in the last d digits and the first d digits.
    # Then we add the two results.
    # The time complexity of this solution is O(2^n) and the space complexity is O(n)
    return 0, 0
