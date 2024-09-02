

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

    assert n >= 1
    fib = [1, 1]
    i = 2
    while i < n:
        fib.append(fib[i-1] + fib[i-2])
        i += 1
    for i in range(n):
        if fib[i+1] > fib[i] and is_prime(fib[i+1]):
            return fib[i+1]
    return fib[-1]
