def largest_divisor(n):
    """
    Find the largest divisor of n less than n.
    """
    for i in range(1, n):
        if n % i == 0:
            return i