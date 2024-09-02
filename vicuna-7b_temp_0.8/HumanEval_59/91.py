

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Try using Sieve of Eratosthenes
    n_prime = 2
    for i in range(n, 0, -1):
        if n % i:
            n_prime = i
            break
    if n_prime > n:
        return n_prime

    # Try using trial division
    while True:
        if n > 2:
            if n % 2:
                return n
        n += 1

    # Try using brute force
    candidates = [2, 3]
    while len(candidates) < n:
        for i in range(1, int(n**0.5) + 1):
            for x in candidates:
                if x % i == 0:
                    candidates.append(i)

    largest_prime = max(candidates, key=len)
    return largest_prime
