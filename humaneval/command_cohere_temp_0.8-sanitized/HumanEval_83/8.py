def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Create a list to store the results for both starting and ending with 1.
    # Assuming the digits are numerically ordered when converting from a string to an integer.
    result = [1] + [0] * (n - 1) + [1]
    return sum(result)