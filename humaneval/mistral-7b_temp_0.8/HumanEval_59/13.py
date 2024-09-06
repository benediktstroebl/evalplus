

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize factors as an empty list.
    factors = []

    # Iterate through integers from 2 to the floor of the square root of n.
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by i, add i to factors.
        if n % i == 0:
            factors.append(i)

    # If factors is not empty, return the largest factor.
    if factors:
        return max(factors)
    # Otherwise, return n.
    return n

