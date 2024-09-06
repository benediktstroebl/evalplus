

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
    if n < 2:
        return 2
    elif n < 5:
        return 1
    else:
        fib = (1, 1)
        for i in range(2, n):
            for j in range(i + 1, n):
                if fib[0] <= (j**2 - i**2) % (j + 1) or fib[1] <= (j**2 - i**2) % (j + 1) :
                    fib = (fib[1], fib[0] + 1)
                    break
        return fib[1]
