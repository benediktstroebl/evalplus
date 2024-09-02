

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    max_p = 0
    while n % 2 == 0:
        max_p = 2
        n /= 2
    for x in range(3, int(n ** 0.5) + 1, 2):
        while n % x == 0:
            max_p = x
            n /= x
    if n > 2:
        max_p = n
    return max_p

