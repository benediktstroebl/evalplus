

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
    if n < 2:
        raise ValueError('n should be >= 2')
    n -= 2

    f = [1, 1]
    while True:
        # Done after the loop because next_fib is called n-times
        if is_prime(f[n]):
            return f[n]
        f.append(next_fib(f[-1], f[-2]))

