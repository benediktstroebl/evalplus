

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Divide by smallest factors first.
    # If we encounter a prime factor, replace n with the quotient.
    # If n is not divisible by 2, then we only have to check odd numbers.
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
