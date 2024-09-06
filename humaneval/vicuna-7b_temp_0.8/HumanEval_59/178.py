

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Note: This is not the most efficient way to solve this problem.
    # This solution uses the sieve of Eratosthenes to find all prime numbers less than n.
    # Then it compares the first n/2 numbers with 2 and keeps the larger one.
    # This approach is simple and easy to understand, but it is not the most efficient.
    # A more efficient solution would be to use the Miller-Rabin primality test.

    n += 1

    # Use the sieve of Eratosthenes to find all prime numbers less than n.
    is_prime = [True] * (n//2)
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p-1]:
            for i in range(p**2, n+1, p):
                is_prime[i] = False

    # Find the largest prime factor of n by comparing the first n/2 numbers with 2.
    largest = 2
    for i in range(n//2, n+1):
        if n//i > 2 and n//i != 2:
            largest = i

    return largest
