
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Discount the zero-length number
    n -= 1
    # Count the number of numbers with 1 at position n
    result = n // 3
    # Discount the number of numbers that start with 1
    result -= n // 4
    # Discount the number of numbers that end with 1
    result -= n // 9
    # Discount the number of numbers that start and end with 1
    result -= n // 36
    # Count the number of numbers that start with 1 and end with 1
    result += n // 12
    return result
