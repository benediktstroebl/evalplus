
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Test the corner cases.
    if n == 0:
        return 1

    # Find the number of digits that start with 1 and the number of digits
    # that end with 1.
    result = 0
    for digit in range(1, n + 1):
        # Calculate the number of numbers that start with 1 and end with digit.
        result += (10 ** (n - digit)) * digit

    # Add the number of numbers that start with digit and end with 1.
    result += ((10 ** (n - 1)) * n)

    return result

