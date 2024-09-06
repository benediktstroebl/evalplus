

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    max_prime = 0
    i = 2
    end = n
    while True:
        if n % i == 0:
            max_prime = i
            n = n / i
            i = 2
        else:
            i += 1
        if n == 1:
            break
    if max_prime == 0:
        max_prime = n
    return max_prime
