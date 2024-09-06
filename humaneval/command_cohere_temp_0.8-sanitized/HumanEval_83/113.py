def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    if n == 1:
        return 9
    if n == 2:
        return 89
    digits = [0] * (n + 1)
    for i in range(1, n + 1):
        digits[i] = digits[i - 1] + 10
    return digits[n]  # Count of numbers that start with 1 + numbers that end with 1