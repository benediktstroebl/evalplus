
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # For numbers of n digits, the largest possible is 1...9.
    # Then add one extra to the number of numbers that end with 1.
    return sum(10**i for i in range(n - 1)) + 10**n
