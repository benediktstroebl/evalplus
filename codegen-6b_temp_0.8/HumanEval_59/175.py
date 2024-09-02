

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    if n % 2 == 1:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return i
        return n
    else:
        return 2
