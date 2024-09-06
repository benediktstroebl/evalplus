

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
    # Check prime number
    if n % 2 == 0:
        return 0
    else:
        f1 = 0
        f2 = 1
        limit = int(n**0.5)
        while True:
            f3 = f1 + f2
            if (n % f3) == 0:
                return 0
            if (f3 > limit):
                f1 = limit
            if (f3 > n):
                f2 = limit
            else:
                f2 = n
        return f3