

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

    fib = [1, 1]
    i = 2
    while i <= n:
        next_fib = fib[i-1] + fib[i-2]
        fib.append(next_fib)
        if is_prime(next_fib):
            i += 1

    return fib[n]

