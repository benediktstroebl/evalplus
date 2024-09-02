

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
    fib = [0, 1]
    while len(fib) < n:
        nxt = fib[-1] + fib[-2]
        if nxt > 1 and nxt % 2 == 0:
            nxt += 1
        fib.append(nxt)
    fib = [n for n in fib if n % 2 != 0]
    return fib[n - 1]

