

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
    pf, pp = 1, 1
    pfp = 0
    while True:
        pfp, pf = pf, pf + pfp
        pp += 1
        if is_prime(pf):
            if pp == n:
                return pf

