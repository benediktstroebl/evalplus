

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    largest_prime_factor = 1
    # for each prime factor of n
    # find all prime factors of n
    for i in range(2, n+1):
        # find the greatest integer that divides n
        while n % i == 0:
            largest_prime_factor = i
            n //= i
        if n == 1:
            return largest_prime_factor
    # if we get here, n is prime and is less than 2
    return n

