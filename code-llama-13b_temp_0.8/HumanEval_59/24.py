

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # First, find the smallest factor
    for i in range(2, n):
        if n % i == 0:
            smallest = i
            break
    # If we did not find a factor, we can return n.
    # Otherwise, we have to repeat the same algorithm.
    if smallest != n:
        return largest_prime_factor(smallest)
    else:
        return n

