

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # print(n)
    if is_prime(n):
        return n

    for i in range(n//2, 2, -1):
        if n % i == 0:
            return largest_prime_factor(i)

