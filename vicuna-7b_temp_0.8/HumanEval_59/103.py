

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Use Sieve of Eratosthenes to find prime numbers up to n
    prime_numbers = [True] * (n + 1)
    for p in range(2, n + 1):
        if prime_numbers[p]:
            for i in range(p ** 2, n + 1, p):
                prime_numbers[i] = False
    largest_prime = 0
    for i in range(1, n + 1):
        if prime_numbers[i]:
            largest_prime = max(largest_prime, i)
    return largest_prime
