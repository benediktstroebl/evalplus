

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
    n = n - 1
    fib = [0, 1]
    i = 2
    while len(fib) < n + 1:
        fib.append(fib[i - 1] + fib[i - 2])
        if is_prime(fib[-1]):
            i = i + 1
    return fib[n]

