def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Define the range of n-digit numbers.
    num_range = list(range(10**(n-1), 10**n, 1))
    # Count the numbers that start or end with 1.
    return sum(1 for num in num_range if num % 10 == 1)