

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
    fib_max = 10**100
    fib = [0, 1] + [0]*(n-1)
    for fib_num in range(2, 1+ n):
        fib_num, fib_i = fib[fib_max]+fib[fib_max-2], fib_max
        fib.append(fib_num)
        fib_max += fib_i
    return fib[-1]
