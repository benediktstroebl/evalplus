

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check for prime candidates under 1000
    primes = [i for i in range(1, 1000) if not i in [2, 3, 5, 7, 11, 13]]
    # Use binary search to find the largest prime factor
    max_diff = 1
    max_index = len(primes) - 1
    while max_diff > 0:
        mid_index = (max_index - max_diff // 2) // 2
        if primes[mid_index] * primes[mid_index + max_diff] > n:
            max_diff //= 2
        else:
            max_index = mid_index
    return primes[max_index]
