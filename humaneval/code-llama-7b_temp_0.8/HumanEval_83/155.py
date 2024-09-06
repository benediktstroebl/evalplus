
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Start with 1-digit integers
    count = (n - 1) // 2
    # Add 2-digit integers
    count += 2
    # Remove 3-digit integers with 1 on both ends
    count -= 1
    return count
