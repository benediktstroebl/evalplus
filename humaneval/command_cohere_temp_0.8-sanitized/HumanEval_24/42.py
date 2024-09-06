def largest_divisor(n):
    """ For a given number n, return the largest divisor of n that is smaller than n, or None if n is prime """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
    return None