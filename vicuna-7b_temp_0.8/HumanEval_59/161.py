

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Find all prime numbers up to sqrt(n)
    prime_numbers = [p for p in range(1, int(n ** 0.5) + 1) if not n % p]

    # Find the largest prime in the list and multiply it by a factor
    # to ensure that n is not a prime
    largest_prime = max(prime_numbers, key=prime_numbers.index)
    n_factors = 0
    while largest_prime <= sqrt(n):
        factors = [2, 3]
        while len(factors) < n_factors:
            i = (int(np.random.random_normal() * (len(factors) - n_factors)) + n_factors) % len(factors)
            factors.append(factors[i])
        smallest_factor = min(factors)
        if smallest_factor > largest_prime / 2:
            break
        largest_prime = largest_prime * largest_prime % n
        n_factors += 1

    # Return the largest prime factor as a positive integer
    return largest_prime
