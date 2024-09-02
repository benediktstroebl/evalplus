

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
    fib = [2, 3]
    for i in range(2, n):
        if fib[-1] % 2 == 0:
            fib.append(fib[-2] + fib[-1])
        else:
            fib.append(fib[-2] + 2 * fib[-1])
        fib = list(filter(lambda x: x % 2 == 1 and all(i % x != 0 for i in fib[:-1]), fib))
    return fib[-1]

