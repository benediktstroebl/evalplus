

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

    pn = 2  # p_n: prime number
    fn = 1  # f_n: Fibonacci number
    fpn = 1  # f_p_n: Fibonacci prime number

    while n > 1:
        fn, pn = fn + fpn, pn
        if is_prime(pn):
            fpn = fn
            n = n - 1
    return pn

