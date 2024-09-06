

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    largest_prime = 2  #largest_prime is 2
    while n % 2 == 0:  #while n is even...
        n /= 2  #divide n by 2
    while n > 1:  #while n > 1
        if n % largest_prime == 0:  #if n is divisible by largest_prime...
            n /= largest_prime  #divide n by largest_prime
        else:
            largest_prime = next_prime(largest_prime)

    return int(largest_prime)

