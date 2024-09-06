

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
    if n in [3, 5]:
        return 2
    while True:
        a, b = n - 1, 1
        while a > 1 and b > 1:
            if a % b == 0:
                a, b = b, a + b
            else:
                if (a, b) in _fibonacci:
                    return int(a)
                a += 1
                b += 1
        if (a, b) in _fibonacci:
            return int(a)
        a += 1
        b += 1
