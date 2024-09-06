

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check that n is not a prime
    if n > 1 and not n % 2:
        return 2
    # Try to find the largest prime factor using trial division
    while True:
        # Check if n is a prime
        if n > 1 and not n % 2:
            # If n is not divisible by any other number, it is a prime
            if n == 2:
                # In this case, 2 is the largest prime factor of n
                return 2
            # If n is divisible by 3, it is not a prime
            elif n % 3 == 0:
                return 3
            # Try the next odd number
            else:
                for i in range(5, int(n ** 0.5) + 1, 2):
                    if n % i == 0:
                        return i
    # If we reach this point, we have not found a prime factor, so return 2
    return 2