

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
    a, b = 0, 1
    fib = [0, 1]
    while fib[-1] <= n:
        a, b = b, a + b
        if b == n:
            return b
        if is_prime(b):
            fib.append(b)
    return n

