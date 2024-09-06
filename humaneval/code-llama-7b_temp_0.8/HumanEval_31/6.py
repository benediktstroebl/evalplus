

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

    # if n < 2:
    #     return False
    # if n in [2, 3, 5, 7]:
    #     return True
    # if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    #     return False
    # if n % 2 == 0 or n % 3 == 0:
    #     return False
    # for i in range(11, int(n ** 0.5), 2):
    #     if n % i == 0:
    #         return False
    # return True

    # for k in range(2, int(n**0.5)+1):
    #     if n % k == 0:
    #         return False
    # return True

    # return all(n % i for i in range(2, int(n**0.5)+1))

    # for k in range(1, int(n**0.5)):
    #     if n % k == 0:
    #         return False
    # return True

    return n >= 2 and all(n % i for i in range(2, n))

