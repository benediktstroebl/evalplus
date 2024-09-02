

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
    # fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
    # if n = 1:
    if n == 1:
        return 2
    elif n == 2:
        return 3
    # f(1) = 1
    f0, f1 = 1, 1
    # if n = 1:
    for i in range(1, n):
        # f(n) = f(n - 1) + f(n - 2)
        f0, f1 = f1, f1 + f0
    # if n = 2:
    if n == 2:
        return 3
    else:
        # if f(n) is prime
        for x in range(3, f1, 2):
            if f1 % x == 0:
                return prime_fib(n - 1)
            else:
                return f1
