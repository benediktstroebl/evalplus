

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
    assert(n > 0)
    if n == 1:
        return 2
    if n == 2:
        return 3
    a = 2
    b = 3
    p_last = 2
    while True:
        p = a + b
        if is_prime(p):
            if p == n:
                return p
            p_last = p
        a, b = b, p
        if p > n:
            break
    p = p_last + (n-p_last)
    if is_prime(p):
        return p
    return n
