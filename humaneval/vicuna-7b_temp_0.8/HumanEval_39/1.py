

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
    if n < 2:
        return 2
    else:
        fib = 0
        n1 = (n - 1) // 2
        n2 = n1 + 1
        while True:
            if n % fib:
                break
            if n % (fib * 2 - fib - 1):
                break
            fib += 1
        return fib
