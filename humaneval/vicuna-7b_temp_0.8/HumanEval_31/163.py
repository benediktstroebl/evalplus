

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
    # Here we use the Sieve of Eratosthenes to quickly determine if a number is prime.
    # This algorithm uses the fact that the prime numbers are distributed randomly among the integers,
    # so there are not many prime numbers close together.
    # The algorithm builds a table of prime numbers, using the following criteria:
    # - all multiples of 2 are prime
    # - all multiples of 3 are also prime
    # - if a number is not divisible by 2 or 3, then it is prime
    # - if a number is divisible by 2, it is not prime
    # - if a number is divisible by 3, then it is divisible by 3 and not prime
    # - if a number is not divisible by 4, then it is prime
    # - if a number is divisible by 4, then it is divisible by 2 and 2 is divisible by 4, so it is not prime
    # - if a number is not divisible by 6, then it is prime
    # - if a number is divisible by 6, then it is divisible by 2 and 3 and not prime
    # - ...
    # - if a number is divisible by 5, then it is prime
    # - if a number is not divisible by 5, then it is not prime
    # - if a number is prime, then it is also the next prime number

    # We use the following steps to determine if a number is prime:
    # 1. If the number is not divisible by 2 or 3, then it is prime.
    # 2. If the number is divisible by 2, then it is not prime.
    # 3. If the number is divisible by 3, then it is divisible by 3 and not prime.
    # 4. If the number is divisible by 4, then it is not prime.
    # 5. If the number is divisible by 5, then it is prime.
    # 6. If the number is divisible by 6, then it is divisible by 2 and 3 and not prime.
    # 7. If the number is divisible by 7, then it is not
