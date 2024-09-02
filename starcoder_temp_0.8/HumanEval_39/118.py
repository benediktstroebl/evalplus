

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
    fib = [1, 2]
    i = 0
    while len(fib) <= n:
        fib.append(fib[i] + fib[i+1])
        i += 1

    for i in range(len(fib) - 1, 0, -1):
        if is_prime(fib[i]):
            return fib[i]
