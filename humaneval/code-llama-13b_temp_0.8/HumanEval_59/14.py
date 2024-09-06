

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    result = 0
    i = 1
    while True:
        i += 1
        if n % i == 0:
            result = i
            while n % i == 0:
                n /= i
        if i >= n:
            break
    return result

