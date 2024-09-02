

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
    # This is a simple sieve to check if a number is prime or not.
    # The algorithm is called Sieve of Eratosthenes and is a classic one.

    # base case: if n <= 3, it's prime.
    if n <= 3:
        return True

    # for all odd numbers > n, it's not prime.
    for i in range(2, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    # for all even numbers < n, it's not prime.
    for i in range(2, int(n**0.5) - 1, 2):
        if n % i == 0:
            return False

    # The number is prime.
    return True
