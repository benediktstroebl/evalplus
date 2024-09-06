

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
    # A number is prime if it is divisible only by 1 and itself.
    # To check for divisibility by 1, we simply check if the number is even.
    # To check for divisibility by 2, we check if the remainder is 0 after dividing.
    # To check for divisibility by any other number, we check if the remainder is 0 after dividing that number.
    # To check if the number is odd, we check if the remainder is 1 after dividing the number by 2.

    # If the number is positive and odd, it is prime.
    if n > 1 and n % 2 == 1:
        return True

    # If the number is positive and even, it is not prime.
    if n > 1 and n % 2 == 0:
        return False

    # If the number is 2, it is prime.
    if n == 2:
        return True

    # If the number is 3, it is not prime.
    if n == 3:
        return False

    # If the number is composite (not prime), we can use the Sieve of Eratosthenes
    # to quickly generate all prime numbers up to the square root of n.
    # Then, we can check if the number is one of those prime numbers.
    for p in primes(n):
        if n == p:
            return False

    # If no prime number up to the square root of n has been found,
    # the number is prime.
    return True
