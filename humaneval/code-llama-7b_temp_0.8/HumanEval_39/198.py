

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
    p_fib = 2
    fib_n = 3
    while True:
        if is_prime(fib_n):
            p_fib = fib_n
        fib_n += 1
        if p_fib >= n:
            break
    return p_fib

