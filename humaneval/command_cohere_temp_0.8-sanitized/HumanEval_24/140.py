def largest_divisor(n):
    """
    Finds the largest divisor of n that is less than n.
    """
    for i in range(1, n):
        if n % i == 0:
            return i
    return 1