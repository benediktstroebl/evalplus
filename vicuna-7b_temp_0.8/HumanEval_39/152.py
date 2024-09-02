

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
    if n < 3:
        return 1
    if n % 2 == 0:
        return 0
    if n > 25:
        return 1
    fib_series = [0, 1, 1, 2, 1, 2, 3, 1, 3, 5, 2, 5, 8, 3, 8, 13, 5, 13, 21, 8, 21, 34, 1, 34, 55, 2, 55, 89]
    for i in range(n // 2):
        if prime_factors(n)[0] != prime_factors(fib_series[i])[0]:
            return 1
    return 0