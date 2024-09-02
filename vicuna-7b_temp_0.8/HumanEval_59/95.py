

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Use the Sieve of Eratosthenes to find all prime numbers up to sqrt(n)
    # in O(sqrt(n)) time.
    prime_count = 0
    for i in range(int(n**0.5) + 1):
        if n % i:
            break
    else:
        prime_count = int(n**0.5) + 1
    
    # Iterate through the remaining numbers up to n and find the largest
    # prime factor.
    largest_prime = 0
    for i in range(prime_count, n + 1):
        if not n % i:
            largest_prime = max(largest_prime, i)
    return largest_prime