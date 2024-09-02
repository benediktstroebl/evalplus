

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
    assert 0 < n <= 10
    f = [2, 3]
    fn = 3
    while fn < n:
        fn = f[-1] + f[-2]
        for p in f:
            if fn % p == 0:
                break
        else:
            f.append(fn)
    return f[-1]
