

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
    assert isinstance(n, int), 'n should be an integer'
    assert n > 0, 'n should be positive'
    fib_seq = (1, 1)
    for i in range(1, n):
        if fib_seq[i] % 2 == 0:
            fib_seq[i] += 1
        while not is_prime(fib_seq[i]):
            fib_seq[i] += fib_seq[i - 1]
    return fib_seq[n - 1]

