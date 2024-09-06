

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
    pn = 0
    fn = 1
    pn_next = 1
    fn_next = 1

    for i in range(1, n):
        pn, fn = pn_next, fn_next
        pn_next = pn + fn
        fn_next = fn + pn

    return pn_next
