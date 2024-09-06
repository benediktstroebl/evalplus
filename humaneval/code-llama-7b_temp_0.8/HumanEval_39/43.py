

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
    if n == 1:
        return 2
    if n == 2:
        return 3

    a = 1
    b = 2
    while True:
        a, b = b, a+b

        if prime_check(b) and prime_check(b+1):
            n = n - 2
            if n <= 0:
                return b
