

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # Create two static lists to store computed primes and Fibonacci numbers
    primes = [2, 3, 5, 7, 11, 13, 17]
    fibs = [1, 2, 3, 5, 8]
    i = 0
    while i < n:
        # append new prime number
        new_prime = primes[-1] + 2
        while not is_prime(new_prime):
            new_prime += 2
        primes.append(new_prime)
        # append new Fibonacci number
        new_fib = fibs[-1] + fibs[-2]
        fibs.append(new_fib)
        i += 1
    return fibs[-1]

