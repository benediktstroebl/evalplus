

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def is_prime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    largest = 0
    i = 2
    while n > largest and i <= n:
        if n % i == 0:
            largest = i
            while n % i == 0:
                n //= i
        i += 1

    if n > largest:
        return largest
    else:
        return n

