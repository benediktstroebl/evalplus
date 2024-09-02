

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
    a, b, i, j = 2, 3, 3, 4
    while a < n:
        if is_prime(a):
            print(a)
        a, b = b, a + b
        i, j = j, i + j
    return b

