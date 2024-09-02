

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
    # This is a basic implementation of the Sieve of Eratosthenes algorithm
    # for primality testing. It has a time complexity of O(k \* log^2 n),
    # where k is the number of prime numbers up to n that need to be tested.
    # This means that it is efficient for small values of n, but becomes
    # impractical for large values of n.
    # 
    # A faster and more efficient algorithm for primality testing is
    # the Miller-Rabin primality test, which has a time complexity of
    # O(k^2 \* log n), where k is the number of test cases that need to be
    # run. However, this implementation uses a simple implementation
    # of the Miller-Rabin primality test that only checks for primality
    # up to 2^32 - 1, which is the maximum value of n that can be represented
    # in Python.

    # The Sieve of Eratosthenes algorithm works by creating a sieve array
    # of size n, where the first n elements are 0, and the next n elements
    # are 1. For each element i in the range 2 to n, if i is prime, then
    # all multiples of i up to n are marked as 0 in the sieve array.
    # This means that if n is prime, then all elements in the sieve array
    # below it will be 0, and all elements above it will be 1.

    # We can then test if n is divisible by any of the elements in the sieve array
    # by checking if any of the elements below it are 0. If there are no 0 elements
    # below n, then n is prime.

    # We can also use the sieve array to quickly find all prime numbers up to n.

    # To use the sieve array to find all prime numbers up to n, we can loop
    # through all the elements in the sieve array and add them to a list if
    # they are prime.

    # For example, to find all prime numbers up to 1000, we can use the sieve array:

    n = 1000
    prime
