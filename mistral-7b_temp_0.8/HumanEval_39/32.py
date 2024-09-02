

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
    if n <= 2:
        return n
    a, b = 2, 3
    while True:
        a, b = b, a + b
        if a <= n:
            if not any(a % k == 0 for k in range(2, a // 2 + 1)):
                return a

