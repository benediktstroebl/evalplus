

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
    
    # # case 1
    # if n == 1:
    #     return False
    # if n == 2:
    #     return True
    # else:
    #     if n % 2 == 0:
    #         return False
    #     else:
    #         return is_prime(n - 1)

    # # case 2
    # if n == 2:
    #     return True
    # elif n > 2:
    #     if n % 2 == 0:
    #         return False
    #     else:
    #         return is_prime(n - 1)

    # # case 3
    # if n <= 1:
    #     return False
    # else:
    #     if n == 2:
    #         return True
    #     elif n % 2 == 0:
    #         return False
    #     else:
    #         return is_prime(n - 1)

    # # case 4
    # if n < 2:
    #     return False
    # else:
    #     if n == 2:
    #         return True
    #     elif n % 2 == 0:
    #         return False
    #     else:
    #         return is_prime(n - 1)

    # # case 5
    # if n <= 1:
    #     return False
    # else:
    #     if n == 2:
    #         return True
    #     elif n % 2 == 0:
    #         return False
    #     else:
    #         return is_prime(n - 1)

    # # case 6
    # if n <= 1:
    #     return False
    # else:
    #     if n == 2:
    #         return True
    #     elif n % 2 == 0:
    #         return False
    #     else:
    #         return is_prime(n - 1)

    # case 7
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        return is_prime(n - 1)

