

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
    if n <= 1:
        return n
    if n <= 2:
        return 2
    f, a, b = fib(n)
    i = 0
    prime = True
    while i < n - 2:
        if f % i:
            prime = False
            break
        i += 1
    if prime:
        return f
    else:
        for j in range(2, n):
            if f % j:
                return f
        return 2 * f

prime_fib_cache = {}
