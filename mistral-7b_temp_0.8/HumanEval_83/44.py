
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Use recursion to iterate through all 10 digits.
    # Example: The count of n-digit numbers that start with 1,
    #   is the count of (n-1)-digit numbers + the count of (n-1)-digit
    #   numbers that start with 1.
    count = 0
    def helper(n):
        # Base case: If n is 1, return 1.
        if n == 1:
            return 1
        # Recursive case: Return 10 * helper(n-1) if n is greater than 1.
        else:
            return (10 * helper(n-1)) + (helper(n-1) if n % 10 == 1 else 0)
    return helper(n)

