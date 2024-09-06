

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
    # Use the Sieve of Eratosthenes to find all prime numbers less than or equal to N.
    # This will speed up the algorithm for large N, but for small N, it is more efficient to
    # use a brute force approach.
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    # Use the sieve to find all prime numbers less than N/2.
    p = 2
    while p*p <= n:
        if n % p == 0:
            break
        p += 1
    if p > n//2:
        return True
    # Check all even numbers between n and 2N.
    for i in range(n//2, n+1, 2):
        if (i + 1) % 2 == 0:
            return False
    return True
