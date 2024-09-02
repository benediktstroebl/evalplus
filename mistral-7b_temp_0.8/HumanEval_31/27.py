

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
    # Count divisors
    for n in range(2, n):
        if n ** 2 >= n:
            break
        if n == 1:
            continue
        if n == 2:
            continue
        if n ** 2 >= n:
            break
        if n % n == 0:
            continue
        if n ** 2 >= n:
            break
        if n % n == 0:
            continue
        if n ** 2 >= n:
            break
        if n % n == 0:
            continue
        if n ** 2 >= n:
            break
        if n % n == 0:
            continue
        if n ** 2 >= n:
            break
        if n % n == 0:
            continue
        if n ** 2 >= n:
            break
        if n % n == 0:
            continue
        if n ** 2 >= n:
            break
        if n % n == 0:
            continue
        if n ** 2 >= n:
            break
        if n % n == 0:
