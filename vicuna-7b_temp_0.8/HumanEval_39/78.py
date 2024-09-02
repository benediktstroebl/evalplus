

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
        raise ValueError("n should be at least 2")
    if n == 2:
        return True
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if fib(i) % n != 0:
                return True
        return False
