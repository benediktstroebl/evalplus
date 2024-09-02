

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

    if n <= 2:
        return 2
    fib_number = prime_fib(n - 1) + prime_fib(n - 2)
    i = 2
    while True:
        if is_prime(fib_number):
            return fib_number
        else:
            i += 1
            fib_number = fib_number + i

