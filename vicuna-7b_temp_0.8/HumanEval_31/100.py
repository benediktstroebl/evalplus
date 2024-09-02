

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
    # TODO: Implement the prime number checking algorithm
    # The Sieve of Eratosthenes is a well-known algorithm for finding all prime numbers up to a given limit.
    # However, we only need to check the prime numbers up to 100, so we can use a simpler approach.
    # One simple way to check if a number is prime is to divide it by all prime numbers less than or equal to its square root, and see if any of them evenly divides the number.
    # For example, if we want to check if 11 is prime, we can divide it by 2, 3, 5, 7, 11, and see if any of them evenly divide the number (which is 11).
    # Since 3 divides 11, but 11 doesn't evenly divide 3, we can conclude that 11 is prime.
    # We can write this as a function:
    def is_prime(n, sqrt_max=100):
        """Return true if a given number is prime, and false otherwise.
        Args:
            n (int): the number to check for primality
            sqrt_max (int): the maximum integer to consider for checking primality.
        """
        if n <= 1:
            return False

        # TODO: Implement the primality test
        # One simple test is to check if n is divisible by any integer greater than sqrt(n),
        # since if n is divisible by an integer greater than sqrt(n), it must also be divisible by 1,
        # since the fractional part of n/d is less than 1/d for any d greater than sqrt(n).
        # However, this test is not reliable for large numbers, since there may be many integers greater than sqrt(n)
        # that divide n, and we may not be able to find them all.
        # A better approach is to use the Sieve of Eratosthenes, which generates a list of prime numbers up to a given limit and uses it to check for primality.
        # We can use the same list of prime numbers for all numbers up to sqrt_max, since we only need to check for primality up to
