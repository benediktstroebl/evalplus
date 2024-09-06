
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Base case
    if n == 1:
        return 1
    # Loop case
    else:
        # Count of numbers starting with 1
        count = (1 << n) - 1
        # Count of numbers ending with 1
        count += sum(1 for i in range(1, n+1) if i % 10 == 1)
        return count
