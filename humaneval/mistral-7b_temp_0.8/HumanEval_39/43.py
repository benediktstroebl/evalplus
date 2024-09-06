

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
    result = []
    a = 0
    b = 1
    i = 0
    while i < n:
        if b > 1 and not any(b % m for m in range(2, b)):
            result.append(b)
            i += 1
        a, b = b, a + b
    return result[n - 1]

