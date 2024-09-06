def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a string of n digits
    num = '1' * n

    # Calculate the two possible cases for starting and ending with 1
    endings_with_1 = len(num) - 2
    starts_with_1 = 1 if n >= 2 else 0

    return endings_with_1 + starts_with_1