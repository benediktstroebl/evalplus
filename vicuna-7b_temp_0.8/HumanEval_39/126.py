

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
        return 0
    if n == 2:
        return 1
    if n in [2, 3]:
        return 2
    if n % 2 == 0:
        return 0
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i:
            continue
        for j in range(i, int(n ** 0.5) + 1, 2):
            if j != i and n % j:
                return 0
        return i