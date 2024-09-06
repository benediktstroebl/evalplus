

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
    # Let's start by checking if the number is even.
    if n % 2 == 0:
        # if it's even, it's not prime, so we return False
        return False

    # 1 is not prime, so we check if n is 1.
    if n == 1:
        # if n is 1, we return False
        return False

    # Otherwise, we check all of the possible divisors from 2 to sqrt(n).
    # If any of them divide n, then we return False.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # if any of them divide n, we return False
            return False

    # If we make it to the end without returning False, then the number is prime.
    # We return True.
    return True

