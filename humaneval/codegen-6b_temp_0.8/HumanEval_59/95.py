

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    i = 2
    if n == 1:
        print('1 is the lt, is prime')
        return 1
    else:
        while n > 1:
            if n % i == 0:
                n = n / i
                count = 2
        return count
