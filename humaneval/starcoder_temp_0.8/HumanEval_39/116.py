

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
    fib_num = 1
    while True:
        fib_num = fib(fib_num)
        if isprime(fib_num):
            if n == 1:
                return fib_num
            else:
                n = n-1
