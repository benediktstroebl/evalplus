

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
    assert 1 <= n <= 10**5, 'n must be in range of [1, 10**5]'
    fib = [1, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    for i in range(n+1):
        if fib[i] > 1 and all(i % k for k in range(2, int(fib[i]**0.5) + 1)):
            return fib[i]

