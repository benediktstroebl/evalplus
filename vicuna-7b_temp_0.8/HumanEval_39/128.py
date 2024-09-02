

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
    if n < 2 or n > 100:
        raise ValueError("Invalid input")

    fib = [0, 1]
    for _ in range(n-1):
        fib.append(fib[0] + fib[1])

    for num in range(2, n):
        if fib[0] * fib[1] % num == 0:
            return 0
        if fib[0] % num == 0 and fib[1] % num == 0:
            return 0
        fib[0] += fib[1]
        fib[1] = 0

    return fib[0]