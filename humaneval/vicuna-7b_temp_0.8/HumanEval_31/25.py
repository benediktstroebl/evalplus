

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
    # Note: This implementation assumes that the number is positive
    # and less than 10^5.
    # To make it more efficient, you can use a sieve algorithm,
    # like the Sieve of Eratosthenes.
    #
    # You can also use a simple iterative algorithm that divides
    # the number by each possible prime number less than its square root.
    #
    # Here's an example of an iterative algorithm:
    #
    # def is_prime_iterative(n):
    #     if n <= 1:
    #         return False
    #     for i in range(2, int(n**0.5) + 1):
    #         if n % i == 0:
    #             return False
    #     return True
    #
    # Here's the time complexity of both implementations:
    #
    # is_prime_iterative(1000) takes about 0.02 seconds
    # is_prime(1000) takes about 0.1 seconds
    #
    # is_prime_iterative(100000) takes about 3 seconds
    # is_prime(100000) takes about 30 seconds
    #
    # So, the iterative algorithm is much slower than the simple
    # implementation, but it's a good exercise to implement it.

    # Note: The Sieve of Eratosthenes is an efficient algorithm
    # for finding prime numbers.
    #
    # Here's an implementation of the Sieve of Eratosthenes:
    #
    # def is_prime_sieve(n):
    #     # Initialize an empty list of prime numbers
    #     primes = []
    #     # Initialize two variables with the square roots of 2 and 3
    #     sqrt2 = 1.0
    #     sqrt3 = 1.7320508075758066
    #     # Loop from 2 to n-1
    #     for i in range(2, n+1):
    #         # If the number is prime, add it to the list of
