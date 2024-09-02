

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    #Returns the largest prime factor of n, -1 if n is prime
    if n == 1:
        return -1
    else:
        max = 0
        for i in range(2,int(sqrt(n))+1):
            if n % i == 0:
                if isPrime(i):
                    max = i
        if max == 0:
            return -1
        else:
            return max
