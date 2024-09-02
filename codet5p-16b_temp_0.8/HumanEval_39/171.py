

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

    p, q, r, p_prime = 1, 1, 0, False
    for i in range(n):
        p, q, r = p + q, p, q
        if r > 1:
            p_prime = True
            continue
    return p if p_prime else 89
