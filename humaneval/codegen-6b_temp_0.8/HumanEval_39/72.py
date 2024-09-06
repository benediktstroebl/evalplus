

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
    if n == 1:
        return 2
    if n == 2:
        return 3
    last_fn = 1
    last_fp = 2
    counter = 3
    while counter <= n:
        fn = last_fn + last_fp
        fp = last_fp
        last_fn = fn
        last_fp = fp
        counter += 1
    if is_prime(fn):
        return fn
    else:
        return False
