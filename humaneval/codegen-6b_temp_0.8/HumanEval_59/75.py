

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    num = n
    while n >= 2:
        a = 2
        while n % a != 0:
            a += 1
        n //= a
        if n == 1:
            return num
        elif n < num:
            num = n
    return num

