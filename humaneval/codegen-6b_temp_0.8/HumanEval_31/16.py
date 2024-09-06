

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
    # The Sieve of Eratosthenes
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        limit = int(sqrt(n))
        t = [True for i in range(n+1)]
        t[0], t[1] = False, False
        for i in range(2, limit+1):
            if t[i]:
                t[i*i:n+1:i] = [False] * len(range(i*i, n+1, i))
        return t[n]
