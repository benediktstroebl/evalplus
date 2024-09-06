

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # base case: 2 and 3 are always prime
    if n == 2 or n == 3:
        return True

    # for larger numbers, use a sieve to check divisibility
    # this is an implementation of the sieve of Eratosthenes
    # which is an efficient algorithm for finding prime numbers
    sieve_of_eratosthenes = [True for i in range(2, n + 1)]
    for p in range(2, int(n**0.5) + 1):
        for i in range(p - 1, n - p - 1, 2):
            sieve_of_eratosthenes[i] = False
    return not any(sieve_of_eratosthenes[i] for i in range(n))
