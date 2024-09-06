

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # TODO: Implement this function
    # Hint: use the Sieve of Eratosthenes to create a list of primes
    #       use the list to filter all non-prime factors

    # returns the largest prime factor of n
    def largest_prime_factor_helper(n):
        # check if n is prime
        if n == 1:
            return
        # create a list of primes up to n
        primes = list(range(2, n + 1))
        for i in range(len(primes)):
            # check if the first element is not a prime
            # if it is, then it is the largest prime factor of n
            if primes[i] == 1:
                continue
            # if the first element is a prime, it is the largest prime factor of n
            if primes[i] == n:
                return n
            # filter all non-prime factors of n
            for j in range(i + 1, len(primes)):
                if primes[j] % primes[i] == 0:
                   
