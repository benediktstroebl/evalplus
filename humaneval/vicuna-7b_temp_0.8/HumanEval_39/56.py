

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
    if n < 4:
        return n
    if n % 2 == 0:
        return 0
    if n == 5:
        return 3
    if n % 3 == 0:
        return 0
    if n == 8:
        return 13
    if n % 13 == 0:
        return 0
    for i in range(13, n + 1, 13):
        if i % 2 == 0:
            continue
        for j in range(13, i + 1, 13):
            if (j - i) % 2 == 0:
                continue
            if (j - i) % i == 0:
                continue
            return j
    return None
