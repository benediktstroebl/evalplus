

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # prime check
    prime_num = n
    if n < 2:
        return n
    # find a factor
    i = 2
    while i ** 2 <= n:
        if prime_num % i == 0:
            prime_num //= i
            i = 2
        else:
            i += 1
    return prime_num

