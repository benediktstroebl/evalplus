def largest_divisor(n):
    """
    Find the largest divisor of n less than n.
    """
    for i in range(2, n):
        if n % i == 0:
            return i
    return 1