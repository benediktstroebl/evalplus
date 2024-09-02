

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(k):
        "Return True if k is a prime number."
        if k == 2:
            return True
        if k % 2 == 0 or k < 2:
            return False
        # n ** 0.5 is square root of n
        for i in range(3, int(n**0.5) + 1, 2):
            if k % i == 0:
                return False
        return True
    if n <= 3:
        return n
    i = 3
    while i*i <= n:
        if n % i == 0 and is_prime(i):
            n //= i
        else:
            i += 2
    return n
