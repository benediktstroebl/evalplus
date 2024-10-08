

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
    if n == 1:
        return 2
    fib = [2, 3]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
        for j in range(2, int(fib[i] ** 0.5) + 1):
            if fib[i] % j == 0:
                break
        else:
            return fib[i]

