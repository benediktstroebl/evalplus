

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

    if n < 1:
        raise ValueError("n must be greater or equal to one")
    if n == 1:
        return 2
    if n == 2:
        return 3

    current = 5
    prime_checker = PrimeChecker()

    while True:
        if prime_checker.is_prime(current):
            if prime_checker.is_fibonacci(current):
                return current
        current += 4

