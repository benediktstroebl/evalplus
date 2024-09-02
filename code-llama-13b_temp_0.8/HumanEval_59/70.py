

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factor = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
            factor = 2
        else:
            for i in range(3, int(math.sqrt(n) + 1), 2):
                if n % i == 0:
                    n //= i
                    factor = i
                    break
            else:
                n = int(n)
                factor = n
    return factor

