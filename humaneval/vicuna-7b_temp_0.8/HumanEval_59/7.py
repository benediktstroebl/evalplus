

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check if n is prime
    if n > 1 and n % 2 == 0:
        return 2

    # Check if n is a prime number
    sieve = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for p in range(i ** 2, n + 1, i):
                sieve[p] = False
    if sieve[n]:
        return n

    # Find the largest prime factor by trial division
    x = 2
    y = n
    while y > 1:
        if y % x == 0:
            x += 1
        elif x * x > y:
            y = x
        else:
            n = y
            break
    return n
