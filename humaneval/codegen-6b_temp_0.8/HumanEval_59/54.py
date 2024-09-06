

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            k = int(n / i)
            if k > i:
                return i
            else:
                return k
        i += 1
