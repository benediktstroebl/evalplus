

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    "*** YOUR CODE HERE ***"
    i = n
    while i > 1:
        if n % i == 0:
            if i % 2 == 0:
                i = i / 2
            else:
                i = i - 1
        else:
            i = i - 1
    return i
    

