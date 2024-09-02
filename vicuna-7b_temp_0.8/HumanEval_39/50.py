

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
    # Check if n is a prime number
    if n % 2 == 0:
        return 0
    # Check if n is a Fibonacci number
    if n == fib(n):
        return 0
    # Check if n is prime
    for i in range(n-1, -1, -1):
        if (n % i) == 0:
            return 0
    # Return the n-th prime number that is a Fibonacci number
    return prime_fib(n-2) + prime_fib(n-1)
