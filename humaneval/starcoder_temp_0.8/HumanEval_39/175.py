

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
    fibs = fibonacci_generator()
    fib_num = next(fibs)
    primes = prime_generator()
    prime_num = next(primes)
    for i in range(n - 2):
        fib_num = next(fibs)
        prime_num = next(primes)
        while prime_num <= fib_num:
            prime_num = next(primes)
    return fib_num
