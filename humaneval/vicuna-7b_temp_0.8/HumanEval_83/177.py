
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Base case: n == 1
    if n == 1:
        return 1
    # Otherwise, 1 <= n <= 9
    else:
        # Find the count of n-digit positive integers that start with 1
        count_starts = (n//10) * (n//10) * (n//10)
        # Find the count of n-digit positive integers that end with 1
        count_ends = (n//10) * (n//10)
        # Return the sum of the counts of the numbers of n-digit positive
        # integers that start and end with 1
        return count_starts + count_ends