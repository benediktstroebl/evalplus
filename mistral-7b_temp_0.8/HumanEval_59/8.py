

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # if n is a prime number, return n
    if n == 2 or n == 3:
        return n
    elif n == 1 or n < 2:
        return None

    # find out the square root of n
    sqrt_n = int(n ** 0.5)

    # check if n is divisible by 2
    if n % 2 == 0:
        return 2

    # check if n is divisible by 3
    if n % 3 == 0:
        return 3

    # check if n is divisible by a prime number less than or equal to sqrt_n
    for i in range(5, sqrt_n + 1, 6):
        if n % i == 0:
            return i
        elif n % (i + 2) == 0:
            return i + 2

    # if n is not divisible by any prime number less than or equal to sqrt_n
    return None

