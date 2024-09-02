

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
    fib = [0, 1]
    for i in range(n - 1):
        a, b = fib
        fib.append(a + b)
        if fib[-1] % 2 == 0:
            fib[-1] += 1
        for x in range(3, int(fib[-1] ** 0.5) + 1, 2):
            if fib[-1] % x == 0:
                fib[-1] += 1
                break
    return fib[-1]

