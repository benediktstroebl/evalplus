def largest_divisor(n):
    """
    Finds the largest divisor of n less than n itself.
    """
    for i in range(1, n):
        if n % i == 0:
            return i