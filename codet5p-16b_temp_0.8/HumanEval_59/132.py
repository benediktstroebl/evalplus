

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    "*** YOUR CODE HERE ***"
    result = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            result = i
            n //= i
        else:
            i += 1
    if n > 1:
        result = n
    return result
