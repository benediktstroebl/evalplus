

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Use the Sieve of Eratosthenes to find the prime numbers up to n
    sieve = [True for i in range(n + 1)]
    sieve[0] = sieve[1] = sieve[2] = True
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            sieve[i] = False
    for i in range(int(n ** 0.5) + 1, n + 1):
        if sieve[i]:
            for j in range(i - 1, -1, -1):
                if sieve[j] and sieve[i] % j == 0:
                    sieve[i] = False
            if sieve[i]:
                prime = i
                while sieve[prime * prime] == False:
                    prime = prime * 2
    return prime
