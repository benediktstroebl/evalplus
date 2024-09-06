

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    max_val = 0
    max_idx = 0
    for val in range(1, n + 1):
        for p in primes[max(0, max_idx - 10) : min(len(primes) - 10, max_idx + 10) + max_val // 2]:
            if val % p == 0:
                break
        else:
            max_val = val
            max_idx = int(log2(max_val) / 3)
    return max_val, max_idx