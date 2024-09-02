

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
    for fib_i in fib():
        if is_prime(fib_i):
            if n == 1:
                return fib_i
            n -= 1
    raise Exception("Not enough Fibonacci numbers")
