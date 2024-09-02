

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    prime = [i for i in range(1, n+1) if is_prime(i)]
    for i in prime:
        if n % i == 0:
            n //= i
        else:
            continue
    return n
