

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
    def prime_fib_generator():
        num = 1
        fib = 1
        while True:
            yield num
            fib, num = num, num + fib
            if num > 1 and is_prime(num):
                yield num
    return next(prime_fib_generator())
