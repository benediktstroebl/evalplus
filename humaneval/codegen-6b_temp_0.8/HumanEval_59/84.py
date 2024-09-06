

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(n):
        if n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
        return True
    i = 2
    while n > 1:
        if is_prime(i) and n % i == 0:
            n = n/i
        else:
            i += 1
    return n

