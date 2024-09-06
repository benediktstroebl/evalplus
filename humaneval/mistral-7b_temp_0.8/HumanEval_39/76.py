

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
    fib_generator = fib()
    i = 0
    while True:
        fib_num = next(fib_generator)
        if is_prime(fib_num):
            return fib_num
        i += 1
        if i == n:
            return None
