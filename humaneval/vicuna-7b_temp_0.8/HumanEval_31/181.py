

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
    # Check if the input number is prime
    if n < 2:
        return False
    elif n in (2, 3):
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    elif n <= 8:
        return True
    else:
        # Check if the number has any factors less than or equal to sqrt(n)
        factors = set()
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                factors.add(i)
        return len(factors) == 2
