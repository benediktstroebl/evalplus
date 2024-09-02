
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        raise ValueError('n must be >= 1')

    # Use a list comprehension to iterate over each digit
    # of n to calculate the number of digits needed for
    # each number of digits in the answer.
    return sum([10 ** (n - 1) for n in range(1, n + 1)])

