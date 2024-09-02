

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # TODO: implement this
    # iterate through range of numbers from 2 up to n and check if a number is a prime and whether it is a divisor of n.
    # return the divisor
    for i in range(2, n + 1):
        if n % i == 0:
            if is_prime(i):
                return i

