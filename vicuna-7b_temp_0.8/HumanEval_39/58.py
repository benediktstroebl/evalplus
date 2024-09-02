

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
    elif n < 3:
        return 3
    elif n < 4:
        return 5
    else:
        i = 0
        while i < n:
            if (i * i) % n == 0:
                return False
            i += 1
        return True