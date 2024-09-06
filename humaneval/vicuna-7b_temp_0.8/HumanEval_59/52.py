

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 0
    largest = 1
    while True:
        if n % 2 == 0:
            return largest
        if n % 3 == 0:
            return 3
        for x in range(5, int(n ** 0.5) + 1, 2):
            if n % x == 0:
                return x
        if n > 1000000:
            break
        n = n - 2
        i += 1
        if i > 10:
            break
    
    return 1
