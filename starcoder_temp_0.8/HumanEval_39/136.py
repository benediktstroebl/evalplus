

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
    # A Fibonacci number is a sum of two terms of the Fibonacci sequence,
    # where the second term is always a positive integer.
    fib = fibonacci(n)
    # The first term of the Fibonacci sequence is 1, and the second term is 2.
    # Because the first two Fibonacci numbers are 1 and 2, we can say that
    # the first two Fibonacci primes are 2 and 3.
    if fib == 2:
        return 3
    if fib == 3:
        return 5
    # The third Fibonacci number is 3.
    # A Fibonacci number is a prime number if it is greater than 1.
    # A Fibonacci number is divisible by 3 if it is not a prime number.
    if fib % 3 == 0:
        return prime_fib(n - 1) + 2
    return prime_fib(n - 1) + fib

