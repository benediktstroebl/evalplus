

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 3:
        return 2
    while n % 2 == 0:
        n = n / 2
    i = 1
    j = 1
    while True:
        if n % i == 0:
            n = n / i
            continue
        if i > j:
            break
        n = n * i
        i = i + 1
        j = j + 2
    return j
