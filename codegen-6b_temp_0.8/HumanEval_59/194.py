

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    current = n
    if current == 1:
        return 1
    for i in range(2, current):
        if current % i == 0:
            current /= i
            if current == i:
                return i
    return n

