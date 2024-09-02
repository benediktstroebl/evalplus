

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
    if n <= 1:
        return fib[0]
    if n == 2:
        return fib[1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
        if fib[-1] % 6 != 1 and fib[-1] % 6 != 5:
            fib.pop()
    return fib[-1]

