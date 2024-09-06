

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
    if n <= 1:
        return n

    if n % 2 == 0:
        return 0

    fib_n = fibonacci(n)

    for i in range(3, int(n ** 0.5) + 1):
        if fib_n % i == 0:
            return 0

    for i in range(2, int(n ** 0.5) + 1):
        if i % 2 == 0:
            continue

        if fib_n % i == 0:
            return 0

    return fib_n
