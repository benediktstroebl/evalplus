

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # if n is less than 3, then it is prime, so we return n
    if n < 3:
        return n

    # if n is 2, then it has no prime factors, so we return 2
    if n == 2:
        return 2

    # if n is odd and less than 3, then it is prime, so we return n
    if n % 2 != 0 and n < 3:
        return n

    # if n is 3, then it has 3 as its only prime factor, so we return 3
    if n == 3:
        return 3

    # if n is 4, then it has 2 and 2 as its prime factors, so we return the larger of the two
    if n == 4:
        return max(2, 2)

    # otherwise, we use the sieve of Eratosthenes to find the prime factors of n
    sieve = [True for i in range(1, int(n**0.5) + 1)]
    for p in range(2, int(n**0.5) + 1):
        if p % 2 != 0:
            for q in range(p, int(n**0.5) + 1, p):
                sieve[q] = False
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if sieve[i]:
            factors.append(i)
            break
    return max(factors)
