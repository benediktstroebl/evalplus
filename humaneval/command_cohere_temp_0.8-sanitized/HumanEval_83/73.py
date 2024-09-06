def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Define the generator expression to iterate through numbers.
    numbers = lambda start, end, prefix: map(lambda x: prefix + x if prefix == '1' else x + '1' if prefix == '1' else x, range(10**(n-1)-1, 0, -1))
    # Count the numbers that start or end with 1.
    ones = sum(1 for _ in numbers(1, 1, '1'))
    tens = sum(1 for _ in numbers(1, '1', '1'))
    return ones + tens