

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2 or not n % 2:
        return 2
    while True:
        for i in range(3, int(n ** 0.5) + 1):
            if n % i:
                break
        n = i
        if n > 1000000:
            return n
        for j in range(3, int(n ** 0.5) + 1, 2):
            if n % j:
                break
        n = j
        if n == 2:
            break
    return n
