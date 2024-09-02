

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
    assert n > 0, "n must be positive."
    assert n < 10000, "n must be less than 10000."

    fib = [1, 2]
    while len(fib) < n:
        fib.append((fib[-1] + fib[-2]) % 10)

    return fib[-1]

